from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          primary_key=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['complete']
