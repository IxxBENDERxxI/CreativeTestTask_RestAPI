from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserData, Cities, UserAdverts


admin.site.register(UserAdverts)
admin.site.register(Cities)


class UserInline(admin.StackedInline):
    model = UserData
    can_delete = False
    verbose_name_plural = 'Доп. информация'

#Defined new class for options of user model
class UserAdmin(UserAdmin):
    inlines = (UserInline,)

#Re register user model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
