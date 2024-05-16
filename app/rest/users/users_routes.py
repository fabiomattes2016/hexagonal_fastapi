from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from app.services.ports.users.create_user_service import CreateUserService
from app.domain.users.schemas import CreateUserRequest
from app.deps import createuserservice_with_mongo_dataport
from app.domain.users.responses import UserResponse
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session


user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {'description': 'Não encontrado'}},
)

@user_router.post('', status_code=status.HTTP_201_CREATED)
async def save(data: CreateUserRequest, db: Session = Depends(get_db), service: CreateUserService = Depends(createuserservice_with_mongo_dataport)):
    await service.save(data=data, db=db)

    return JSONResponse({
        'status': 201,
        'message': 'Usuário criado com sucesso.'
    })
