from django.contrib import admin
from .models import ParentNav, SubMenu


# Register your models here.
class navigationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


admin.site.register(ParentNav, navigationAdmin)


class SubNavigation(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


admin.site.register(SubMenu, SubNavigation)
