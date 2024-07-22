from django.contrib import admin
from .models import Email,LinkClick

# Register your models here.
# admin.site.register(Email)
# admin.site.register(LinkClick)
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'sent_at')

@admin.register(LinkClick)
class LinkClickAdmin(admin.ModelAdmin):
    list_display = ('email', 'url', 'click_count')