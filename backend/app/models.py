from sqlmodel import Field, SQLModel

class ErrorRecord(SQLModel, table=True):
    __tablename__ = "errors"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    language: str
    message: str