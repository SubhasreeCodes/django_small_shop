from django.contrib import admin
from django.utils.html import format_html

from backend.models import Category, Brand

# Register your models here.
admin.site.register(Category)
# admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image_tag')

    search_fields = ('id','name')

    def image_tag(self, obj):
        if obj.image_path:
            return format_html('<img src="{}" width="150" height="150" />'.format(obj.image_path.url))
        return "No Image"  # In case there's no image

    image_tag.short_description = 'Image'

admin.site.register(Brand,BrandAdmin)
