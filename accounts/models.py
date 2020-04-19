from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPhotos(AbstractUser):
    user_img = models.ImageField(upload_to='pics/')

