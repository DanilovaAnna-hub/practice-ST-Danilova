from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select

from database.connection import get_session
from models.users import NewUser, User, UserSignIn

user_router = APIRouter(tags=["User"])


@user_router.post("/signup")
async def sign_new_user(data: NewUser, session=Depends(get_session)) -> dict:
    user_exist = session.exec(select(User).where(User.email == data.email)).first()
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует",
        )
    user = User(email=data.email, password=data.password, events=[])
    session.add(user)
    session.commit()
    return {"message": "Пользователь успешно зарегистрирован!"}


@user_router.post("/signin")
async def sign_user_in(data: UserSignIn, session=Depends(get_session)) -> dict:
    user = session.exec(select(User).where(User.email == data.email)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не существует",
        )
    if user.password != data.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверные учётные данные",
        )
    return {"message": "Пользователь успешно вошёл в систему"}
