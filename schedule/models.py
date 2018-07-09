from django.db import models
from uuid import uuid4


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # events = models. TODO: array of Event objects
        created_at = models.DateTimeField(auto_now_add=True)
        last_modified = models.DateTimeField(auto_now=True)
