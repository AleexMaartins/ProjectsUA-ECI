import os
from PIL import Image
import uuid
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow warnings
from deepface import DeepFace
from fastapi import Depends
import matplotlib.pyplot as plt
import shutil
from numpy import asarray
from const.ImageProcessing import Directories
from fastapi.concurrency import run_in_threadpool
from services.S3Service import S3Service
# from services.PhotoService import PhotoService
from models.FaceRecog import FaceRecogRepository
import cv2
# TODO: properly treat types, errors and return!!!!

class FaceRecognitionService:
    def __init__(
        self,
        # photoService: PhotoService = Depends(),
    ):
        # self.photoService = photoService
        self.s3Service = S3Service()
        self.faceRecogRepository = FaceRecogRepository()
        self.imageData = {}

    async def face_recog_alg(self,albumId, imageKeyList, currentUser):
        masterDirName = self.temporary_directories()
        await self.get_person_and_face(albumId, masterDirName)
        await self.run_face_recog(albumId, imageKeyList, currentUser, masterDirName)
        await self.delete_temporary_directories(masterDirName)

    async def run_face_recog(self,albumId, imageKeyList, currentUser, masterDirName):
        for key in imageKeyList:
            img = await self.s3Service.get_image_by_key(key)
            faces = await self.store_faces(asarray(img), masterDirName)
            self.imageData[key] = {  # Use the image key as the key in imageData
                "faces": faces
            }
        for face in os.scandir(masterDirName + os.getenv("FACES")):  # match faces to persons
            namedPerson = self.get_person_by_face(
                face, masterDirName + os.getenv("NAMED_PERSON"))
            if (namedPerson):
                self.assign_face(face, namedPerson)
                self.create_face(face, namedPerson.name, albumId, currentUser)
                print("Face in named group.")
                continue
            nonNamedPerson = self.get_person_by_face(
                face, masterDirName + os.getenv("NON_NAMED_PERSON"))
            if (nonNamedPerson):
                self.assign_face(face, nonNamedPerson)
                self.create_face(face, nonNamedPerson.name, albumId, currentUser)
                print("Face in non named group.")
                continue
            newPersonName, newPersonPath = self.create_person(albumId,masterDirName)
            self.assign_face(face, newPersonPath)
            thumbnailKey = self.create_face(face, newPersonName, albumId, currentUser)
            self.update_person_thumbnail(newPersonName, thumbnailKey)
            print("Face in new group.")

    async def run_search_face(self,face, masterDirName): 
        namedPerson = self.get_person_by_face(
            face, masterDirName + os.getenv("NAMED_PERSON"))
        
        if (namedPerson):
            print("Face in named group.")
            return namedPerson.name
        
        nonNamedPerson = self.get_person_by_face(
            face, masterDirName + os.getenv("NON_NAMED_PERSON"))
        if (nonNamedPerson):
            return nonNamedPerson.name
        return None

    async def store_faces(self, rawImage, masterDirName):
        detectedFaces = None
        # try with "OpenCV's Haar cascades" and "Dlib's HOG" respectively
        for enforce_detection in [True, False]:
            print(f"Trying enforce_detection: {enforce_detection}")
            try:
                detectedFaces = DeepFace.extract_faces(
                    rawImage, enforce_detection=enforce_detection)
                if detectedFaces:
                    break
            except Exception as e:
                print(
                    f"Failed with enforce_detection {enforce_detection}. Error: {str(e)}")

        if not detectedFaces:
            print("No faces detected with any enforce_detection value.")
            return []
        faces = []
        i = 1
        for faceObj in detectedFaces:
            face = faceObj["face"]
            region = faceObj["facial_area"]
            face = face.astype('float32')  # Convert the image to CV_32F depth
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            fig = plt.figure(frameon=False)
            fig.set_size_inches(1, 1)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            region_str = "_".join(f"{key}_{value}" for key, value in region.items() if key not in ['left_eye', 'right_eye'])
            ax.imshow(face, aspect='auto')
            facePath = str(uuid.uuid1()) +"_coords_" + region_str +"_face_"+ str(i) + "_.jpg"
            fig.savefig(os.path.join(masterDirName + os.getenv("FACES"), facePath), dpi=500)
            faces.append(facePath)
            i += 1
        return faces

    def get_person_by_face(self, face, personGroup):
        for person in os.scandir(personGroup):
            for personFace in os.scandir(person):
                result = DeepFace.verify(
                    face.path, personFace.path, enforce_detection=False)
                if result["verified"]:
                    return person
        return None

    def assign_face(self, face, personPath):
        shutil.copy(face, personPath)

    def create_person(self, albumId, masterDirName):
        newPersonName = str(uuid.uuid1())
        newPersonPath = masterDirName + os.getenv("NON_NAMED_PERSON") + newPersonName
        os.makedirs(newPersonPath)
        self.faceRecogRepository.supabase_create_person(newPersonName, albumId)
        return newPersonName, newPersonPath

    def create_face(self, face, newPersonLabel, albumId, currentUser):
        for key in self.imageData.items():
            if face.name in key[1]["faces"]:
                photoKey = key[0]
                break
        # Create the file key
        fileName = face.name
        file_key = f'{currentUser}/{albumId}/faces/{newPersonLabel}/{fileName}'

        # Read the image data as bytes
        with open(face.path, 'rb') as file:
            file_bytes = file.read()
        self.s3Service.upload_image(file_key, file_bytes)
        self.faceRecogRepository.supabase_create_face(photoKey, newPersonLabel,file_key)
        return file_key
    

    def update_person_thumbnail(self, personLabel, thumbnailKey):
        self.faceRecogRepository.supabase_update_person_thumbnail(personLabel, thumbnailKey)

    def temporary_directories(self):
        if not os.path.exists(os.getenv("PHOTO_PROCESSING_DIR")):
            os.makedirs(os.getenv("PHOTO_PROCESSING_DIR"))
        masterDirName =  os.getenv("PHOTO_PROCESSING_DIR") +"/" + str(uuid.uuid1()) + "/"
        os.makedirs(masterDirName)
        os.makedirs(masterDirName + os.getenv("RAW_IMAGES"))
        os.makedirs(masterDirName + os.getenv("NAMED_PERSON"))
        os.makedirs(masterDirName + os.getenv("NON_NAMED_PERSON"))
        os.makedirs(masterDirName + os.getenv("FACES"))
        return masterDirName
        
   
    async def get_person_and_face(self, albumId, masterDirName):
        people = self.faceRecogRepository.supabase_get_person_and_face(albumId)
        
        if not people:
            print("No people found in Supabase")
            return
        
        for person in people:
            if person[1] == None:
                break
            for key in person[1]:
                dir_name = None
                if key['is_named']:
                    dir_name = masterDirName + os.getenv("NAMED_PERSON") + str(key['label'])
                    os.makedirs(dir_name, exist_ok = True) #get person
                else:
                    dir_name = masterDirName + os.getenv("NON_NAMED_PERSON") + str(key['label'])
                    os.makedirs(dir_name, exist_ok = True)
                
                for face in key['Faces']:
                    face_key = face['zoomed_face']
                    face_img = await self.s3Service.get_image_by_key(face_key) 
                    face_img.save(dir_name + '/' + face_key.split('/')[-1])

    async def delete_temporary_directories(self, masterDirName):   
        shutil.rmtree(masterDirName)