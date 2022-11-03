from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'FIO')
    list_display_links = ('id', 'username')
    search_fields = ('id', 'username')


admin.site.register(User, UserAdmin)



