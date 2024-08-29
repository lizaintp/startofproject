from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Create your views here.

from apps.base import models
from apps.base import serializers

class NewArrivalsApi(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):
    queryset = models.NewArrivals.objects.all()
    serializer_class = serializers.NewArrivalsSerializer