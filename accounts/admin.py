from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(MyUser, MyUserAdmin)
