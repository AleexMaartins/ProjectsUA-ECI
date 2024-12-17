from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.AlbumRouter import AlbumRouter
from routers.AuthRouter import AuthRouter
from routers.PhotoRouter import PhotoRouter
from routers.PersonRouter import PersonRouter

# Core Application Instance
app = FastAPI(
    title = "face-finder-api",
    version = "1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Should be changed to only accept our origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routers
app.include_router(AuthRouter)
app.include_router(AlbumRouter)
app.include_router(PhotoRouter)
app.include_router(PersonRouter)