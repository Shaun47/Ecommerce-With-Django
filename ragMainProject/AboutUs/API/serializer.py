from rest_framework import serializers
from ..models import OurStory, OurValuesImg, OurValuesDescription, OurPromisesImg, OurPromisesDescription


class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = ['id','title', 'description', 'img']


class OurValuesImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurValuesImg
        fields = ['id','img']


class OurValuesDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurValuesDescription
        fields = ['id','title', 'description']


class OurPromisesImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPromisesImg
        fields = ['id','img']


class OurPromisesDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPromisesDescription
        fields = ['id','title', 'description']