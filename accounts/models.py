from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError ('Wymagane jest podanie adresu e-mail')
        if not password:
            raise ValueError ('Wymagane jest podanie hasła')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self,email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self,email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField (db_index=True, unique=True,max_length=100)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'