from contextlib import asynccontextmanager
from typing import Annotated

import app.models
from fastapi import Depends, FastAPI #FastAPI를 가져온다
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from app.database import create_db_and_tables, get_session
from app.models import ErrorCreate, ErrorRead, ErrorRecord

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

SessionDep = Annotated[Session, Depends(get_session)]

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

@app.post(
    "/api/errors",
    response_model=ErrorRecord,
    status_code=201,
)
def create_error(
    error: ErrorCreate,
    session: SessionDep,
):
    db_error = ErrorRecord(
        title=error.title,
        language=error.language,
        message=error.message,
    )

    session.add(db_error)
    session.commit()
    session.refresh(db_error)

    return db_error

@app.get(
    '/api/errors',
    response_model=list[ErrorRead], #ErrorRead 형태의 데이터 여러 개 들어있는 리스트 응답
)
def get_errors(
    session: SessionDep,
):
    statement = select(ErrorRecord)
    errors = session.exec(statement).all() #ErrorRecord 조회하고 결과 전부 가져와서 error 변수에 저장
    return errors #FastAPI가 JSON으로 바꿔서 사용자에게 전달