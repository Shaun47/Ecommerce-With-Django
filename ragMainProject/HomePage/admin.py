from django.contrib import admin
from .models import Difference, ChooseUs, TopProducts, RequestCall, Footer


# Register your models here.
class differenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')


admin.site.register(Difference, differenceAdmin)


class chooseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')


admin.site.register(ChooseUs, chooseAdmin)


class topProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'img')


admin.site.register(TopProducts, topProductsAdmin)


class callRequestsAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'phone','mail','message')


admin.site.register(RequestCall, callRequestsAdmin)


class footerAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'locationTitle', 'loc1','loc2','loc3', 'contactTitle','mail','phone','logo')


admin.site.register(Footer, footerAdmin)

