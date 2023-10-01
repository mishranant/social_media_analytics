import uuid
from django.db import models

class Post(models.Model):
    def __str__(self):
        return str(self.id + ': ' + self.content)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()