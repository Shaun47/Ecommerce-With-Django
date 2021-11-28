from django.db import models


# Create your models here.


class HomePage(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    paragraph = models.CharField(max_length=5000, blank=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    paragraph = models.CharField(max_length=5000, blank=True)
    img = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    paragraph = models.CharField(max_length=5000, blank=True)
    img = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    paragraph = models.CharField(max_length=5000, blank=True)
    img = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
