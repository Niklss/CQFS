from django.db import models


# Create your models here.
class User_Manager(models.Manager):
    def create_user(self, args):
        sys_user = self.create(first_name=args["first_name"], last_name=args["last_name"], password=args["password"], role=args["role"], group=args["group"])
        return sys_user


class Sys_User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.IntegerField()
    group = models.CharField(max_length=50)

    objects = User_Manager()

def add_user(args):
    user = Sys_User.objects.create_user(args)
    return user
