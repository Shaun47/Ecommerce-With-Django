from django.db import models


# Create your models here.
class OurStory(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class OurValuesImg(models.Model):
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.img


class OurValuesDescription(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class OurPromisesImg(models.Model):
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.img


class OurPromisesDescription(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

