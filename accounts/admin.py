from django.contrib import admin
from django.contrib.auth.models import User as User_admin

# Register your models here.

from .models import User


class PersonAdmin(admin.ModelAdmin):
    list_display = ('email', 'gender', 'role')  # whatever
    search_fields = ('email',)

admin.site.register(User,PersonAdmin)
admin.site.register(User_admin)
