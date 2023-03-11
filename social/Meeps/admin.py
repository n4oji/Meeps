from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

admin.site.unregister(Group)

#mix profile and user
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    #mostrar apenas campo username no admin
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)


