from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
    # Here we are ordering the models, so the latest update will always be at the top
    class Meta:
        ordering = ['-updated']