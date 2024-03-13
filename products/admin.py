from django.contrib import admin
from django.utils.html import mark_safe
from products.models import Category, Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProductInline,]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Наименование и категория', {'fields':('title', 'category')}),
        ('Описание, Картинка, Вес, Состав', {'fields': ('description', 'images', 'dish_weigth', 'structure')}),
        ('Цена и доступность', {'fields':('price', 'availability')}),
    )
    
    list_display = ('title', 'category', 'price', 'availability', 'description', 'product_list_image')
    list_filter = ('category', 'availability',)
    search_fields = ('title',)

    def product_list_image(self, obj):
        return mark_safe(f'<img src = "{obj.images.url}" width = 3% >')
    
    product_list_image.short_description = 'Превью'

  


# Register your models here.
