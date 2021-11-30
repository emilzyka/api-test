from fastapi import FastAPI
from app import models, config
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# To run, put in cmd: uvicorn app.main:app --reload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# Request Get-method url "/", order matters top-down!
@app.get("/")
async def root():
    return {"message": "Welcome to this simple API!"}
