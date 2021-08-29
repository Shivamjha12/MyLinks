# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from .models import Profile

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_or_save_user_profile(created,instance,*args,**kwargs):
#     print("OKAyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
#     if created:
#         print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
#         Profile.objects.create(user=instance)
#     instance.profile.save()
#     print("Byyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")