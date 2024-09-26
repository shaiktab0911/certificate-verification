from django.db import models

class Certificate(models.Model):
    certificate_id = models.CharField(max_length=100, unique=True)
    image_path = models.CharField(max_length=255)
