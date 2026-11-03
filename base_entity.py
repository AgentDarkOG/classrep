class BaseEntity:
    """A lightweight base entity for simple Python models."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return dict(self.__dict__)

    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

    def __eq__(self, other):
        return isinstance(other, BaseEntity) and self.__dict__ == other.__dict__
