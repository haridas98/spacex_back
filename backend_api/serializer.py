from rest_framework import serializers
from .models import NavbarItem, Adv

class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        fields = ['id', 'name', 'url', 'is_active', 'is_hidden']

class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'text1', 'number', 'text2']