from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    attachement = models.FileField(upload_to = 'uploads/', null=True)