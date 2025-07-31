from django.contrib import admin
from .models import Screenshot

@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ["screenshot", "created"]
    readonly_fields = ["created"]