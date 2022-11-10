from django.contrib import admin
from staff.models import Staff, JobTitle, SubDivision


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'FIO', 'user', 'office_apteka', 'job_title', 'sub_division')
    list_display_links = ('id', 'FIO')
    search_fields = ('id', 'FIO')
    # list_editable = ('available',)
    # list_filter = ('available', 'category', 'brand', 'unit')


class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class SubDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Staff, StaffAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(SubDivision, SubDivisionAdmin)

