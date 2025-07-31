from django.db import models
from datetime import date
import os

def get_upload_path(instance, filename):
    today = date.today()
    return os.path.join(f'screenshots/{today}/', filename)

class Screenshot(models.Model):
    screenshot = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    created = models.DateTimeField("created", auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Screenshot from {self.created}"