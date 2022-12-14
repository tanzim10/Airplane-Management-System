from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_num = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender =User)
    def create_profile(sender,instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, created, **kwargs):
        user = instance
        if created:
            profile = User(user=user)
            profile.save()






