from django.contrib import admin
from .models import ( 
    Product, ProductImage, Comment, 
    ViewedProduct, NewArrival, Discount, SaleOff
)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    search_fields = ('category', 'name')
    list_filter = ('category',)

    class Meta:
        model = Product

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_on', 'active')
    # search_fields = ('product', )
    list_filter = ('active', 'created_on')

    filter_horizontal = ()
    fieldsets = ()

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

# admin.site.register(ViewedProduct)

admin.site.register(NewArrival)
admin.site.register(Discount)
admin.site.register(SaleOff)