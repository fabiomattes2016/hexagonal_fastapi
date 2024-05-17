from fastapi import APIRouter, status, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.deps import gettokenservice, getrefreshtokenservice, verifytokenservice
from app.domain.authentication.responses import TokenResponse

from app.services.ports.authentication.get_token_service import GetTokenService
from app.services.ports.authentication.get_refresh_token_service import GetRefreshTokenService
from app.services.ports.authentication.verify_token_service import VerifyTokenService


auth_router = APIRouter(
    prefix="/auth",
    tags=["Autenticacao"],
    responses={404: {'description': 'Não encontrado.'}}
)


@auth_router.post("/token", status_code=status.HTTP_200_OK, name="authenticate_user", description="Faz a autenticação e retorna o token e o refresh token.", response_model=TokenResponse)
async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), service: GetTokenService = Depends(gettokenservice)):
    return await service.get_token(data=data, db=db)


@auth_router.post("/refresh", status_code=status.HTTP_200_OK, name="refresh_token", description="Atualiza o token de autenticação.", response_model=TokenResponse)
async def refresh_token(refresh_token: str = Header(), db: Session = Depends(get_db), service: GetRefreshTokenService = Depends(getrefreshtokenservice)):
    return await service.get_refresh_token(refresh_token, db)


@auth_router.post("/verify", status_code=status.HTTP_200_OK, name="verify", description="Verifica se um token é válido.")
async def verify(token: str = Header(), db: Session = Depends(get_db), service: VerifyTokenService = Depends(verifytokenservice)):
    return await service.verify_token(token, db)
