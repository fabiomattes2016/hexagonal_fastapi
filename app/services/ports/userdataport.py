from abc import ABC, abstractmethod


class UserDataPort(ABC):
    @abstractmethod
    async def save(object, db):
        pass
