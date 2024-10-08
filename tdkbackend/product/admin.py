from django.contrib import admin
from .models import Product,Category,Service
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category','quantity','image_url','active','price','discount')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active','image_url')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active','image_url')
# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)