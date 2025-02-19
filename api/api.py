from api.dependencies import get_api_key
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Security
from api.routes import tables

app = FastAPI(
    dependencies=[Security(get_api_key)]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tables.router)

@app.get("/")
def read_root():
    return