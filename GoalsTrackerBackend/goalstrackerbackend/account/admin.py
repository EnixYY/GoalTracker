from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AccountAdmin(UserAdmin):

    list_display = ('email', 'name', 'role', 'department')
    search_fields = ('email', 'name', 'role', 'department')
    readonly_fields = ('id',)
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'name', 'role', 'department')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'name', 'role', 'department', 'password')}),
    )


admin.site.register(Account, AccountAdmin)