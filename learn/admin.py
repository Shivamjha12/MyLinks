from django.contrib import admin
from learn.models import *

# Register your models here.
class UserBioAdmin(admin.ModelAdmin):
    readonly_fields= ('dateAndTime',)

admin.site.register(Contact)
admin.site.register(CreateUserBio, UserBioAdmin)
admin.site.register(Images)
admin.site.register(Profile)
# admin.site.register(otherUserDetails)