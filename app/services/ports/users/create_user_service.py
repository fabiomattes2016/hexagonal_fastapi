from abc import ABC, abstractmethod


class CreateUserService(ABC):
    @abstractmethod
    async def save(data, db):
        pass
