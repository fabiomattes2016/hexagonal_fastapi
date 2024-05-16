from abc import ABC, abstractmethod


class SqliteDataPort(ABC):
    @abstractmethod
    async def save(object, db):
        pass
