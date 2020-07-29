from django.db import models


# Create your models here.

class User(models.Model):
    choice = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(null=False, blank=False, max_length=20, unique=True)
    gender = models.CharField(max_length=32, choices=choice, default='男')
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=11)
    create_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
