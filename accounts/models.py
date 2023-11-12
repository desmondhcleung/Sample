from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone1 = models.CharField(max_length=50, default='')
    phone2 = models.CharField(max_length=50, default='')
    mail_address = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
