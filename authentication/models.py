from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='uploaded_image/user')