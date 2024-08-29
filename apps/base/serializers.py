from rest_framework import serializers

from apps.base import models

class NewArrivalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewArrivals
        fields = ['id', 'title', 'description', 'image']