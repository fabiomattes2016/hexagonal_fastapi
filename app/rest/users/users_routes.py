from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from app.services.ports.users.create_user_service import CreateUserService
from app.domain.users.schemas import CreateUserRequest
from app.deps import createuserservice
from app.domain.users.responses import UserResponse
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.infrastructure.security import oauth2_scheme
from app.domain.users.responses import CreateUserResponse


user_router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {'description': 'Não encontrado.'}},
)

private_user_router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {'description': 'Não encontrado.'}},
    dependencies=[Depends(oauth2_scheme)]
)


@user_router.post('', status_code=status.HTTP_201_CREATED, name="save", description="Cria um novo usuário.", response_model=CreateUserResponse)
async def save(data: CreateUserRequest, db: Session = Depends(get_db), service: CreateUserService = Depends(createuserservice)):
    await service.save(data=data, db=db)

    return JSONResponse({
        'status': 201,
        'message': 'Usuário criado com sucesso.'
    })


@private_user_router.post('/me', status_code=status.HTTP_200_OK, name="get_user_details", description="Retorna os dados do usuário logado.", response_model=UserResponse)
def get_user_details(request: Request):
    return request.user
