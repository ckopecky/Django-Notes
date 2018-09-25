from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4 

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title=models.CharField(max_length=140)
    content=models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title

    class Meta:
        ordering= ('title',)


class PersonalNote(Note):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    