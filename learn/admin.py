from django.contrib import admin
from learn.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserBioAdmin(admin.ModelAdmin):
    readonly_fields= ('dateAndTime',)
class profileInline(admin.TabularInline):
    model = Profile # one_to_one_field or foreign_key


class UserAdmin(UserAdmin):
    model = User
    list_display = ('first_name','username','is_staff',)
    list_filter = ('first_name','username','is_staff',)
    fieldsets = (
                    (None,{'fields':('first_name','username','password')}),
                    ('permissions',{'fields':('is_staff',('is_superuser','is_active'), )}),
                    ('Important dates',{'fields':('date_joined',)}),
                    ('Advanced options',
                    {
                        'classes': ('collapse',),
                        'fields':  ('groups','user_permissions'),
                    
                    }),
                
                )
    add_fieldsets = (
        
        (None,{
            'classes':('wide',),
            'fields':('username','password1','password2','is_staff','is_active','is_superuser','groups')
        }),
    )
#chan
    inlines =[
        profileInline
    ]



    # def get_profile(self,obj): # this function only work in list_display
        # return obj.Profile  # we using here reverse relationship



# admin.site.register(Contact)
# admin.site.register(CreateUserBio, UserBioAdmin)
# admin.site.register(Images)
# admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
# admin.site.register(otherUserDetails)
