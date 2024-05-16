from abc import ABC, abstractmethod
from app.domain.users.models import UserModel


class AuthenticationDataPort(ABC):
    @abstractmethod
    async def get_token(data, db):
        pass


    @abstractmethod
    async def get_refresh_token(token, db):
        pass


    @abstractmethod
    async def verify_token(token, db):
        pass
