from base_entity import BaseEntity


class Book(BaseEntity):
    def __init__(self, id=None, title=None, author=None, description=None, **kwargs):
        super().__init__(
            id=id,
            title=title,
            author=author,
            description=description,
            **kwargs,
        )

    def __repr__(self):
        return (
            f"Book(id={self.id!r}, title={self.title!r}, "
            f"author={self.author!r}, description={self.description!r})"
        )


__all__ = ["Book"]
