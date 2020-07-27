from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(User):
    # self
    username = User.username
    password = User.password
    email = User.email
    tell = models.IntegerField(unique=True, blank=False, null=False, verbose_name='手机号')
    # type = Us/

    def __str__(self):
        return self.username
