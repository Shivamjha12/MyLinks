from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.fields import URLField
from PIL import Image
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
# Create your models here.
class Contact(models.Model):
    name  = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc  = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email

class Createuserform(UserCreationForm):
    class Meta:
        models   = User
        fields   = ['username','first name','last name','email','password1','password2']
    def fullname(self):
        fullname = self.first_name + ' ' + self.last_name
        return fullname






category_choices= (
    ('Motion_icon', 'Motion Icon'),
    ('Important_icon','Important'), 
)

class CreateUserBio(models.Model):
    title              = models.CharField(max_length=32,default='My new link')
    addSocialMediaLink = URLField()
    link_icon          = models.CharField(max_length=100,default="",blank=True,choices=category_choices)
    image              = models.ImageField(upload_to='media/img/',blank=True,null=True,default="/static/img/avatarLogo.jpg")
    dateAndTime        = models.DateTimeField(auto_now_add=True)
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    page_views         = models.IntegerField(blank=True, null=True,default="0" )
    
    def __str__(self):
        return self.title

class Images(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    ProfileImage = models.ImageField(blank=False,null=True, default="/static/img/avatarLogo.jpg")
    
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user       = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image      = models.ImageField(default='avatarLogo.jpg', upload_to='media/img/')
    story      = models.CharField(max_length=50, default="Hii i am using InstaBio",blank=True)
    Proffesion = models.CharField(max_length=100,default="",blank=True,verbose_name="Your Proffesion")
    adress     = models.CharField(max_length=100,default="",blank=True,verbose_name="Adress")



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, ** kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_save_user_profile(created,instance,*args,**kwargs):
    print("OKAyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    if created:
        print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        Profile.objects.create(user=instance)


    # instance.profile.save()
    # print("Byyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        
    # get_username = user.cleaned_data.get('username')
    # x = User.objects.values('id').filter(username=get_username).first()
    # p=Profile(user_id=x['id'])
    # p.save()
    # x = User.objects.values('id').filter(username=username).first()
    # bio_data = CreateUserBio.objects.filter(user=x['id'])
    # print(x)




# @receiver(post_save, sender=User,dispatch_uid='save_new_user_profile')
# def create_or_save_profile(sender,created,instance,*args,**kwargs):
#     super(Profile).save(*args, **kwargs)
#     print("HELLO")
    # if created:
    #     Profile.objects.create(user=instance)
    #     profile = Profile(user=user)
    #     Profile.save()

# class otherUserDetails(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     story = models.CharField(max_length=50, default="Hii i am using InstaBio",blank=True)
#     Proffesion = models.CharField(max_length=100,default="",blank=True)
#     adress = models.CharField(max_length=100,default="",blank=True)
    # adress = models.CharField()
# class UserDetail(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
#     Name = models.CharField(max_length=25)
#     Description = models.TextField(null=True, blank=True)
#     profile_image = models.ImageField(null=True, blank=True)
#     email = models.EmailField( null=True, blank=True)
#     dateAndTime = models.DateTimeField(auto_now_add=True, null=True)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, default="")


    