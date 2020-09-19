from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('shopuser', 'product',)


# 등록하기
admin.site.register(Order, OrderAdmin)
