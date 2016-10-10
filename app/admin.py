from django.contrib import admin

# Register your models here.
from app.models import App, Version


class AppAdmin(admin.ModelAdmin):
    pass
class VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(App, AppAdmin)
admin.site.register(Version, VersionAdmin)