from app.services.ports.sqlitedataport import SqliteDataPort
from app.services.ports.users.create_user_service import CreateUserService


class CreateUserServiceImpl(CreateUserService):
    def __init__(self, sqliteport: SqliteDataPort) -> None:
        self.sqliteport = sqliteport

    async def save(self, data, db):
        return await self.sqliteport.save(data, db)
