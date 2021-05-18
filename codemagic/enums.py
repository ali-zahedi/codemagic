import enum


class ChoicesMeta(enum.EnumMeta):
    """A metaclass for creating a enum choices."""

    def __contains__(cls, member):
        if not isinstance(member, enum.Enum):
            # Allow non-enums to match against member values.
            return any(x.value == member for x in cls)
        return super().__contains__(member)


class Choices(enum.Enum, metaclass=ChoicesMeta):
    """Class for creating enumerated choices."""

    def __str__(self):
        """
        Use value when cast to str, so that Choices set as model instance
        attributes are rendered as expected in templates and similar contexts.
        """
        return str(self.value)

    def __eq__(self, other):
        """Overrides the default implementation"""
        return str(self.value) == str(other)
