from abc import ABC, abstractmethod


class VerifyTokenService(ABC):
    @abstractmethod
    async def verify_token(token, db):
        pass