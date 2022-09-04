from django.contrib import admin
from users.models import Profile


admin.site.register(Profile)

class Profile_admin(admin.ModelAdmin):
    list_display = ['name','surname','birth_date', 'address']
