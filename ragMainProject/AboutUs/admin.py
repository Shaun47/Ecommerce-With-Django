from django.contrib import admin
from .models import OurStory, OurValuesImg, OurValuesDescription, OurPromisesImg, OurPromisesDescription


# Register your models here.
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'img')


admin.site.register(OurStory, OurStoryAdmin)


class OurValuesImgAdmin(admin.ModelAdmin):
    list_display = ('id','img')


admin.site.register(OurValuesImg, OurValuesImgAdmin)


class OurValuesDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(OurValuesDescription, OurValuesDescriptionAdmin)


class OurPromisesImgAdmin(admin.ModelAdmin):
    list_display = ('id','img')


admin.site.register(OurPromisesImg, OurPromisesImgAdmin)


class OurPromisesDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(OurPromisesDescription, OurPromisesDescriptionAdmin)