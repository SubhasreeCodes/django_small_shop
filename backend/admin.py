from django.contrib import admin
from django.utils.html import format_html

from backend.models import Category, Brand, Product, Cart, Order, OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'id',)

    # Add filters for name field
    list_filter = ('name',)

    # Add search for name field
    search_fields = ('name',)

    # Sorting by name in ascending order
    ordering = ['name']

    # To sort by name in descending order, use the negative sign
    # ordering = ['-name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # You can customize the queryset here, e.g., add annotations or filters
        return qs.filter(is_published=False)

admin.site.register(Category,CategoryAdmin)

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

admin.site.register(Product)

admin.site.register(Cart)

admin.site.register(Order)

admin.site.register(OrderItem)
