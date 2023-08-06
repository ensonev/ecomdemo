from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['customer', 'name', 'active', 'created_at']
    raw_id_fields = ('customer',)
    list_filter = ('name','category')
    readonly_fields = ('created_at','updated_at')
  
    