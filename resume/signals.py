from django.db.models.signals import post_delete, post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Contact



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user=instance
    if created:
        profile=Profile.objects.create(user=user)


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    instance.user.delete()


@receiver(post_save, sender=Contact)
def contact_mail(sender, created, instance, **kwargs):
    obj=instance
    if created:
        send_mail('Portfolio Contact Form',
                    obj.text, 'portfolio@gmail.com', ['benyamin.az@hotmail.com'])