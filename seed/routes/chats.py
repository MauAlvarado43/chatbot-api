"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Chat
from app.serializers import ChatSerializer

class ChatViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Chat.filter_permissions(
            super().get_queryset(), Chat.permission_filters(user))