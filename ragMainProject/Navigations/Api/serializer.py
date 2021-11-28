from rest_framework import serializers
from ..models import ParentNav, SubMenu


class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentNav
        fields = ['id', 'name', 'slug','hasChild']


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id', 'name', 'slug','parentNav_id']
