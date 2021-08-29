from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from learn.models import *
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
# class EditUserForm(UserChangeForm):
#     class Meta:
#         pass

class UpdateUserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email',]

class ProfileImageUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['story','Proffesion','adress','image',]

# class UserDetails(forms.ModelForm):
#     class Meta:
#         model = otherUserDetails
#         fields = ['story','Proffesion','adress']

class ImagesForm(forms.ModelForm): 
    class Meta: 
        user = Images 
        fields = ['user', 'image'] 

class CreateBioPage(ModelForm):
    class Meta:
        model = CreateUserBio
        fields = ['title', 'addSocialMediaLink','link_icon',]
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'input'}),
        #     'addSocialMediaLink': forms.URLInput(attrs={'class': 'input'}),
        #     # 'ShowOrHide': forms.RadioSelect(attrs={'class': 'boolean'}),


        # }



      