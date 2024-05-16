from app.adapters.sqlite_dataport import SqliteDataAdapter
from app.services.users.create_user_service_impl import CreateUserServiceImpl
from app.services.ports.users.create_user_service import CreateUserService


async def createuserservice_with_mongo_dataport() -> CreateUserService:
    return CreateUserServiceImpl(SqliteDataAdapter())
