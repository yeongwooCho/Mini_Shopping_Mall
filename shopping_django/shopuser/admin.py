from django.contrib import admin
from .models import Shopuser
# Register your models here.


class ShopuserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    # 콤마 안찍으면 tuple이 아니라 문자열 하나로 인식한다


# 등록하기
admin.site.register(Shopuser, ShopuserAdmin)
