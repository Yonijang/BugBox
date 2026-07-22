from contextlib import asynccontextmanager

import app.models
from fastapi import FastAPI #FastAPI를 가져온다
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

app = FastAPI( #우리 백엔드 어플리케이션을 만든다
    title = "BugBox API",
    description = "Backend API for BugBox",
    version = "0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") #/주소로 GET 요청이 들어오면 아래 함수를 실행한다
def root():
    return {
        "message": "BugBox API is running" #JSON 데이터를 돌려준다
    }