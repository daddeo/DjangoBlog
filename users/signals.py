from django.db.models.signals import post_save
from django.contrib.auth.models import User # the sender of the signal
from django.dispatch import receiver # the receiver of the signal
from .models import Profile

# create a user profile for each new user
# when a user is saved send post_save signal which is handled/received by the create_profile
# function. the receiver takes in all the supplied information (instance of the user)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
# kwargs (keyword arguments) captures any additional parameters passed in and not specified
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
