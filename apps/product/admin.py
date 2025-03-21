from django.contrib import admin
from apps.product.models import Product, ProductImage
from django.utils.html import format_html
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height = "50px" />'.format(obj.image.url)) 
    
    image_tag.short_description = "Изображение"
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title', 'price', 'created_at', 'image_tag']
    list_editable = ('price',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    
    inlines = [ProductImageAdmin]
     
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.get_first_image()))
    
    image_tag.short_description = "Изображение"