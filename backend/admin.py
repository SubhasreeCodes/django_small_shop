from django.contrib import admin
from django.utils.html import format_html

from backend.models import Category, Brand, Product, Cart, Order, OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ( 'id','name', 'article_count','description')

    # Specify 'name' as the field to be linked to the change view
    list_display_links = ('id', 'description')

    # Add filters for name field
    list_filter = ('id','name',)

    # Add search for name field
    search_fields = ('name',)

    # Sorting by name in ascending order
    ordering = ['name']

    # To sort by name in descending order, use the negative sign
    # ordering = ['-name']

    # Allow inline editing of the 'name' field
    list_editable = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # You can customize the queryset here, e.g., add annotations or filters
        return qs.filter(is_published=False)

    def article_count(self, obj):
        # Make sure the related manager is correctly referenced, especially if it's a foreign key relation
        return obj.article_set.count()
    # Custom column name
    article_count.short_description = 'Number of Articles'

    def mark_as_published(self, request, queryset):
        queryset.update(is_published=True)
    mark_as_published.short_description = 'Mark selected category as published'

    def mark_as_unpublished(self, request, queryset):
        queryset.update(is_published=False)
    mark_as_unpublished.short_description = 'Mark selected category as unpublished'
    actions = [mark_as_published, mark_as_unpublished]

admin.site.register(Category, CategoryAdmin)

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
