from django.db import models

class Post(models.Model):
    def __str__(self):
        return str(self.id + ': ' + self.content)
    
    content=models.TextField()