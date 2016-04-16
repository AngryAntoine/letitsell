from django.contrib import admin
from .models import Category, Product, Order, OrderItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [('Item', {'fields': [('name', 'slug'), 'category', 'description']}),
                 ('Date information', {'fields': [('created', 'updated')], 'classes': ['collapse']}),
                 ('Medias', {'fields': ['image']}),
                 ('Metas', {'fields': [('status', 'price', 'stock')]}),
                 ]
    readonly_fields = ('created', 'updated')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inline = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
