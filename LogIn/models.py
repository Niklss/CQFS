from django.db import models
from django.shortcuts import get_object_or_404


# Create your models here.
class DBHelper():
    def add_user(self, args):
        user = Sys_User.objects.create_user(args)
        return user

    def is_in_system(self, login, password):
        try:
            user = Sys_User.objects.get(mail=login, password=password)
            return user
        except:
            return None


class User_Manager(models.Manager):

    def create_user(self, args):
        sys_user = self.create(login=args["login"], password=args["password"], first_name=args["first_name"],
                               last_name=args["last_name"], role=args["role"], group=args["group"], mail=args["mail"])
        return sys_user


class Sys_User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()
    group = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)

    objects = User_Manager()
