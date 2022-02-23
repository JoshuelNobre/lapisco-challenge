from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from src.schemas import User as SchemasUser, UserEdit
from src.schemas import UserSimple
from src.repository import UserRepository
from src.config import get_db
from sqlalchemy.orm.session import Session
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post(
    "/usuario",
    tags=["user"],
    response_model=UserSimple,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(user: UserSimple, db: Session = Depends(get_db)):
    user_located = UserRepository(db).get_by_email(user.email)
    if user_located:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail already registered"
        )
    user_created = UserRepository(db).create(user)
    return JSONResponse(
        {"message": " User created"}, status_code=status.HTTP_201_CREATED
    )


@router.get(
    "/users",
    tags=["user"],
    response_model=List[SchemasUser],
    status_code=status.HTTP_200_OK,
)
def get_users(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users


@router.get("/user/{id}", tags=["user"])
def get_user(id: int, db: Session = Depends(get_db)):
    user_located = UserRepository(db).list_by_id(id)
    if not user_located:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There isn't user with id = {id}",
        )
    return user_located


@router.put("/user/edit/{id}", tags=["user"])
def update_user(id: int, user: UserEdit, db: Session = Depends(get_db)):
    user_located = UserRepository(db).list_by_id(id)
    if not user_located:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There isn't user with id = {id}",
        )
    UserRepository(db).edit(id, user)
    return JSONResponse(
        {"message": " User updated successfully"}, status_code=status.HTTP_200_OK
    )


@router.delete("/users/remove/{id}", tags=["user"])
def remove_user(id: int, db: Session = Depends(get_db)):
    user_located = UserRepository(db).list_by_id(id)
    if not user_located:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There isn't user with id = {id}",
        )
    UserRepository(db).remove(id)
    return JSONResponse(
        {"detail": "User deleted successfully", "data": id},
        status_code=status.HTTP_200_OK,
    )
