
from enum import Enum

class Directories(Enum):
    RAW_IMAGES = "temporary_files/raw_images/"
    FACES= "temporary_files/temporary_faces/"
    NAMED_PERSON= "temporary_files/person/true/"
    NON_NAMED_PERSON= "temporary_files/person/false/"
