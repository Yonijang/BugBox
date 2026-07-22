from sqlmodel import Field, SQLModel

class ErrorBase(SQLModel):
    title: str
    language: str
    message: str

class ErrorRecord(ErrorBase, table=True):
    __tablename__ = "errors"

    id: int | None = Field(default=None, primary_key=True)
    
class ErrorCreate(ErrorBase):
    pass