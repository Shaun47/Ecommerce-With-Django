from django.db import models
from django.http import HttpResponse


# Create your models here.
class ParentNav(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60, blank=True)
    hasChild = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    parentNav = models.ForeignKey(ParentNav, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
