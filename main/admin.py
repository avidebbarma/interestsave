from django.contrib import admin
from .models import Profile, MyUserForm1,MyUserForm2, MyUserForm3

# Register your models here

admin.site.register(Profile)
# admin.site.register(MyUserForm)
admin.site.register(MyUserForm1)
admin.site.register(MyUserForm2)
admin.site.register(MyUserForm3)