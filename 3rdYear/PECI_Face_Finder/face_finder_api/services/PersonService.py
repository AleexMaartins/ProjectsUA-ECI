import uuid
from fastapi import Depends, File, HTTPException
from services.S3Service import S3Service
from models.Person import Person, PersonRepository
from middleware.AuthMiddleware import verify_owner, get_user_album_roles
from models.Photo import PhotoRepository

class PersonService:
    def __init__(
        self,
    ):
        self.personRepository = PersonRepository()
        self.s3Service = S3Service()
        self.photoRepository = PhotoRepository()
        
    async def get_album_people(self, albumId, current_user):
        album = await verify_owner(albumId, 'Album', current_user)
        user_roles = await get_user_album_roles(albumId, current_user)
        if album and (album['isPublic'] or album['god_id'] == current_user or any(role in user_roles for role in ['photographer', 'participant', 'admin'])):
            people = self.personRepository.get_people(albumId)
            for person in people:
                person['thumbnail_key'] = self.s3Service.get_photo_url(person['thumbnail_key'])
            return people
        else:
            return {"error": "User does not have the necessary permissions"}

    async def get_person_by_label(self, label):
        person = self.personRepository.get_person(label)
        person['thumbnail_key'] =  self.s3Service.get_photo_url(person['thumbnail_key'])
        return person
    
    async def edit_label(self, newLabel, oldLabel):
        person = self.personRepository.set_label(newLabel, oldLabel)
        return person
    
    async def delete_faces_by_photo(self, photoId):
        faces = await self.personRepository.get_faces_by_photo(photoId)
        for face in faces:
            label = await self.personRepository.get_labels(face['id'])
            person =  await self.personRepository.get_faces_by_person(label)

            print("getperson", person)
            if person is None:
                print("111111111111111111111111111111111111111111111",label)
                label1= label[0]
                print ("label1", label1)
                label2 = label1["person_label"]
                print ("label2", label2)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                await self.personRepository.delete_person(label["person_label"])

            await self.s3Service.delete_image(face['zoomed_face'])
            await self.personRepository.delete_face(face['id'])
        return {"message": "Faces deleted"}
        
    #if person with labels is has no photos, delete person
    def delete_person(self, label):
        self.delete_faces_by_person(label)
        faces = self.personRepository.get_faces_by_person(label)
        if len(faces) == 0:
            self.personRepository.delete_person(label)
        return {"message": "Person deleted"}

    async def get_person_edit_permissions(self, albumId: str, current_user: str):
        print(f"Album ID: {albumId}")
        print(f"Current User: {current_user}")
        album = await verify_owner(albumId, 'Album', current_user)
        print(f"Album: {album}")
        user_roles = await get_user_album_roles(albumId, current_user)
        print(f"User Roles: {user_roles}")
        if album and (album['god_id'] == current_user or any(role in user_roles for role in ['admin'])):
            return {"message": "User has necessary permissions"}
        else:
            raise HTTPException(status_code=403, detail="Not authorized to edit this person")