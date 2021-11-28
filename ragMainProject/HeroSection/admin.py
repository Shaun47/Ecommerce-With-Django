from django.contrib import admin
from .models import HomePage,AboutUs,Services,Contact


# Register your models here.
class homeAdmin(admin.ModelAdmin):
    list_display = ('title', 'paragraph','img')


admin.site.register(HomePage, homeAdmin)


class aboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'paragraph','img')


admin.site.register(AboutUs, aboutAdmin)


class servicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'paragraph','img')


admin.site.register(Services, servicesAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display = ('title', 'paragraph','img')


admin.site.register(Contact, contactAdmin)