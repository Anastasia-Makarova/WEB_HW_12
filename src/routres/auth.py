from datetime import date

from fastapi import APIRouter, HTTPException, Depends, Security, status, Path, Query
from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession


from src.database.db import get_db
from src.repository import users as repository_users
from src.schemas.user  import UserSchema, UserResponse, TokenSchema


router = APIRouter(prefix='/auth', tags=['auth'])

@router.post("/signup")
async def signup(body: UserSchema, db: AsyncSession = Depends(get_db)):
    # exist_user = db.query(User).filter(User.email == body.username).first()
    # if exist_user:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    # new_user = User(email=body.username, password=hash_handler.get_password_hash(body.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    pass
    return {}


@router.post("/login")
async def login(body: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    # user = db.query(User).filter(User.email == body.username).first()
    # if user is None:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    # if not hash_handler.verify_password(body.password, user.password):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    # # Generate JWT
    # access_token = await create_access_token(data={"sub": user.email})
    # refresh_token = await create_refresh_token(data={"sub": user.email})
    # user.refresh_token = refresh_token
    # db.commit()
    pass
    return {}


@router.get('/refresh_token')
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(), db: AsyncSession = Depends(get_db)):
    # token = credentials.credentials
    # email = await get_email_form_refresh_token(token)
    # user = db.query(User).filter(User.email == email).first()
    # if user.refresh_token != token:
    #     user.refresh_token = None
    #     db.commit()
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    # access_token = await create_access_token(data={"sub": email})
    # refresh_token = await create_refresh_token(data={"sub": email})
    # user.refresh_token = refresh_token
    # db.commit()
    pass
    return {}