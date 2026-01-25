from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    cnic = models.CharField(max_length=13, unique=True)
    full_name = models.CharField(max_length=150)
    constituency = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
  

    USERNAME_FIELD = 'cnic'
    REQUIRED_FIELDS = ['full_name','constituency']

    objects = UserManager()

    def __str__(self):
        return self.cnic
