from django.contrib import admin
from . import models

class ForumAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'msg', 'date']

admin.site.register(models.Event)
admin.site.register(models.Team)
admin.site.register(models.HomePageContent)
admin.site.register(models.Forum, ForumAdmin)