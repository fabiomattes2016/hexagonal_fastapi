from abc import ABC, abstractmethod


class GetRefreshTokenService(ABC):
    @abstractmethod
    async def get_refresh_token(data, db):
        pass
