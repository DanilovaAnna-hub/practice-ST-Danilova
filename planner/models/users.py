from sqlmodel import JSON, Column, Field, SQLModel
from typing import List, Optional
from pydantic import ConfigDict, EmailStr

class User(SQLModel, table=True):
    email: EmailStr = Field(primary_key=True)
    password: str
    events: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
    )


class NewUser(SQLModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }
    )


class UserSignIn(SQLModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }
    )
