from sqlmodel import Field, SQLModel

class ErrorBase(SQLModel):
    title: str
    language: str
    message: str

class ErrorRecord(ErrorBase, table=True): #DB내부용 응답 모델
    __tablename__ = "errors"

    id: int | None = Field(default=None, primary_key=True)
    
class ErrorCreate(ErrorBase):
    pass

class ErrorRead(ErrorBase): #API 응답 모델 (사용자에게 보냄)
    id: int