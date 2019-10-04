from api.serializers import UserSerilalizer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerilalizer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
