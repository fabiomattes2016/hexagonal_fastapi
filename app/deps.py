from app.adapters.sqlite_dataport import SqliteDataAdapter
from app.adapters.authentication_dataport import AuthenticationDataAdapter

from app.services.users.create_user_service_impl import CreateUserServiceImpl
from app.services.ports.users.create_user_service import CreateUserService

from app.services.authentication.get_token_service_impl import GetTokenServiceImpl
from app.services.authentication.get_refresh_token_service_impl import GetRefreshTokenServiceImpl
from app.services.authentication.verify_token_service_impl import VerifyTokenServiceImpl
from app.services.ports.authentication.get_token_service import GetTokenService
from app.services.ports.authentication.get_refresh_token_service import GetRefreshTokenService
from app.services.ports.authentication.verify_token_service import VerifyTokenService


async def createuserservice_with_mongo_dataport() -> CreateUserService:
    return CreateUserServiceImpl(SqliteDataAdapter())


async def gettokenservice() -> GetTokenService:
    return GetTokenServiceImpl(AuthenticationDataAdapter())


async def getrefreshtokenservice() -> GetRefreshTokenService:
    return GetRefreshTokenServiceImpl(AuthenticationDataAdapter())


async def verifytokenservice() -> VerifyTokenService:
    return VerifyTokenServiceImpl(AuthenticationDataAdapter())
