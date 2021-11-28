from rest_framework import serializers
from ..models import Difference, ChooseUs, TopProducts, RequestCall, Footer


class DifferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difference
        fields = ['id','title', 'description', 'link']


class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = ['id','title', 'description', 'link']


class TopProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProducts
        fields = ['id','title', 'description', 'img']


class RequestCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestCall
        fields = ['id','firstName', 'lastName', 'phone','mail','message']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id','companyName', 'locationTitle', 'loc1','loc2','loc3','contactTitle','mail','phone','logo']
