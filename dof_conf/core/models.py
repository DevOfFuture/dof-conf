import uuid

from django.db import models

from model_utils.models import TimeStampedModel


class UUIDModel(models.Model):
    """
    An abstract base class with a UUID as primary key.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampedModel):
    """
    An abstract base model with a UUID as primary key plus automatic `created`
    and `modified` fields.
    """
    class Meta:
        abstract = True
