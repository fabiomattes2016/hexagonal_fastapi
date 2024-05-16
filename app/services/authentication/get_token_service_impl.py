from abc import ABC, abstractmethod


class GetTokenService(ABC):
    @abstractmethod
    async def get_token(data, db):
        pass
