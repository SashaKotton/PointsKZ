from django.contrib import admin
from deliverers.models import DeliveryCompany, Deliverer

@admin.register(DeliveryCompany)
class DeliveryCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Deliverer)
class DelivererAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'delivery_company')
    list_filter = ('delivery_company',)
    search_fields = ('name', 'surname', 'phone')

# Register your models here.
