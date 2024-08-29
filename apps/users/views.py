from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

from apps.users import models
from apps.users import serializers
from apps.users.permissions import UserPermission

class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.UserRegisterSerializer
        return serializers.UserSerializer

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
