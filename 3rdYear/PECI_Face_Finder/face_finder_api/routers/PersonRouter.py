from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks
from typing import List
from services.PersonService import PersonService
from services.FaceRecognitionService import FaceRecognitionService
from middleware.AuthMiddleware import get_optional_current_user
from models.Person import EditPerson
from middleware.AuthMiddleware import get_current_authenticated_user

PersonRouter = APIRouter(
    prefix="/person", tags=["person"]
)

@PersonRouter.get("/{albumId}",)
async def get_people(
    albumId: str, 
    current_user: str = Depends(get_optional_current_user), 
    personService: PersonService = Depends()
    ):
    people = await personService.get_album_people(albumId, current_user)
    return people

@PersonRouter.get("/info/{label}",)
async def get_person(label: str, personService: PersonService = Depends()):
    person = await personService.get_person_by_label(label)
    return person

@PersonRouter.post("/edit/",)
async def set_person_label(editObject: EditPerson, personService: PersonService = Depends()):
    person = await personService.edit_label(editObject.newLabel, editObject.oldLabel)
    return person
@PersonRouter.delete("/delete/{photoId}",)
async def delete_faces_by_photo(photoId: str, personService: PersonService = Depends()):
    response = await personService.delete_faces_by_photo(photoId)
    return response

@PersonRouter.get("/editPermissions/{albumId}",)
async def get_person_edit_permissions(
    albumId: str, 
    current_user: str = Depends(get_optional_current_user),
    personService: PersonService = Depends()
    ):
    permissions = await personService.get_person_edit_permissions(albumId, current_user)
    return permissions