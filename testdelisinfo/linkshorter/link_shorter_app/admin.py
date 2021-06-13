from django.contrib import admin

from .models import Link


class AdminUrl(admin.ModelAdmin):
    list_display = ('full_url', 'short_url')


admin.site.register(Link,AdminUrl)