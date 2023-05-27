from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from account.managers import UserManager



# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(upload_to='profile/', blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)