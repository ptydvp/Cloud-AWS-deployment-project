from django.contrib import admin
from webpage.models import restaurant, restaurant_type, restaurant_menu

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant_name', 'desc']
    list_per_page = 10
    list_filter = ['restaurant_name']
    search_fields = ['restaurant_name']
admin.site.register(restaurant, RestaurantAdmin)


class Restaurant_TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']
    list_filter = ['type_name']
    search_fields = ['type_name']
admin.site.register(restaurant_type, Restaurant_TypeAdmin)

admin.site.register(restaurant_menu)