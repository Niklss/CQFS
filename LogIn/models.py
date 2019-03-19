from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, role, username=None):
        user = self.model(email=email, first_name=first_name, last_name=last_name, role=role, password=password,
                          username=username)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if Sys_User.objects.all().count() > 0:
            username = 'user_{}'.format(Sys_User.objects.latest('id').id + 1)
        else:
            username = 'user_1'

        user = self.create_user(email=email, password=password, username=username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class Sys_User(AbstractUser):
    email = models.EmailField(_('email'), max_length=40, unique=True)
    first_name = models.EmailField(_('email'), max_length=40, null=True)
    last_name = models.EmailField(_('email'), max_length=40, null=True)
    role = models.EmailField(_('email'), max_length=40, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomAccountManager()

    class Meta:
        verbose_name = _('User')

    verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
