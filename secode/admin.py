from django.contrib import admin

from secode.models import CodeCheckList, CodeCheck, Code


class CodeCheckInline(admin.TabularInline):
    model = CodeCheck


class CodeCheckListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('BASE INFORMATION', {'fields': ['title']})
    ]
    inlines = [CodeCheckInline]
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ['title']


class CodeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('BASE INFORMATION', {'fields': ['codechecklist', 'code']}),
        ('STATUS', {'fields': ['error']})
    ]
    list_display = ('__str__', 'created', 'updated')
    list_filter = ('created',)


admin.site.register(CodeCheckList, CodeCheckListAdmin)
admin.site.register(Code, CodeAdmin)
