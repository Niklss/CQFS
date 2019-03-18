from django.db import models


# Create your models here.
class DBHelper():
    def add_user(self, args):
        user = Sys_User.objects.create_user(args)
        return user

    def is_in_system(self, login, password):
        user = Sys_User.objects.get(login=login, password=password)
        if user is not None:
            return user
        return False


class User_Manager(models.Manager):

    def create_user(self, args):
        sys_user = self.create(login=args["login"], password=args["password"], first_name=args["first_name"],
                               last_name=args["last_name"], role=args["role"], group=args["group"])
        return sys_user


class Sys_User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()
    group = models.CharField(max_length=50)

    objects = User_Manager()
