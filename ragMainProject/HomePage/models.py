from django.db import models


# Create your models here.
class Difference(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()
    link = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return self.title


class ChooseUs(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()
    link = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return self.title


class TopProducts(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class RequestCall(models.Model):
    firstName = models.CharField(max_length=1000, blank=True)
    lastName = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=1000, blank=True)
    mail = models.CharField(max_length=1000, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.firstName


class Footer(models.Model):
    companyName = models.CharField(max_length=1000, blank=True)
    locationTitle = models.CharField(max_length=1000, blank=True)
    loc1 = models.CharField(max_length=1000, blank=True)
    loc2 = models.CharField(max_length=1000, blank=True)
    loc3 = models.CharField(max_length=1000, blank=True)
    contactTitle = models.CharField(max_length=1000, blank=True)
    mail = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=1000, blank=True)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.companyName
