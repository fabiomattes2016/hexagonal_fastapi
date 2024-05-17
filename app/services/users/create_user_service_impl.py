from app.services.ports.userdataport import UserDataPort
from app.services.ports.users.create_user_service import CreateUserService


class CreateUserServiceImpl(CreateUserService):
    def __init__(self, sqliteport: UserDataPort) -> None:
        self.sqliteport = sqliteport


    async def save(self, data, db):
        return await self.sqliteport.save(data, db)
