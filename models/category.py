from base_entity import BaseEntity


class Category(BaseEntity):
    def __init__(self, id=None, name=None, description=None, **kwargs):
        super().__init__(id=id, name=name, description=description, **kwargs)

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r}, description={self.description!r})"


__all__ = ["Category"]
