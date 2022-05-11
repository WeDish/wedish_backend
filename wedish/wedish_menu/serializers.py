from rest_framework import serializers, permissions
from .models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'recommended_retail_price']
        permission_classes = [permissions.IsAdminUser]
