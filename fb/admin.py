from django.contrib import admin
from .models import*
# Register your models here.
class AdminUserData(admin.ModelAdmin):
    list_display = ['name', 'password','cover_img','user_bio']

class AdminUser(admin.ModelAdmin):
    list_display = ['user_name', 'user_mobile','user_signuppass','user_dateOFbirth','user_gender']

admin.site.register(UserData, AdminUserData)
admin.site.register(User, AdminUser)

