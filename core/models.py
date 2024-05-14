from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(BaseUserManager):
    def email_validation(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide valid email'))

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have email address')
        self.email_validation(email)
        clean_email = self.normalize_email(email)
        user = self.model(email=clean_email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Task(models.Model):
    title = models.CharField(max_length= 254)
    status = models.CharField(max_length= 254)
    datetime = models.DateTimeField()
    # assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email')
