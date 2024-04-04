from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    whatsapp = models.CharField(max_length=15)
