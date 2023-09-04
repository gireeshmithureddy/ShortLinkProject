from django.db import models

# Create your models here.

class ShortLink(models.Model):
    short_code = models.CharField(max_length=10, unique=True)
    long_url = models.URLField(max_length=255)

    def __str__(self):
        return self.short_code