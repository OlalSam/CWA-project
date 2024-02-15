from django.contrib import admin
from userAuth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display  = ['username', 'email']

admin.site.register(User)
# Register your models here.
