from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(max_length=20, default='', help_text='Please input your mobile number')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{str(self.id)}_{self.user.username}_profile'


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='info')
    mail_confirmed = models.BooleanField(default=False)
    black_list = models.BooleanField(default=False)
