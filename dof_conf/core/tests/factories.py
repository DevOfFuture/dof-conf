import factory

from ..models import BaseModel


class BaseFactory(factory.DjangoModelFactory):
    class Meta:
        model = BaseModel
        abstract = True
