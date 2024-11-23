from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"