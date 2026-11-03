from abc import ABC, abstractmethod

from models.books import Book


class IUserRepository(ABC):
    @abstractmethod
    def add_books(self, book: Book) -> None:
        pass


__all__ = ["IUserRepository"]
