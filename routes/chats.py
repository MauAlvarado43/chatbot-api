"""
__Seed builder__
  Extended module
"""

import seed.routes.chats as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Chat
from app.serializers import ChatSerializer
from domain.chatbot import generate_chatbot_response

class ChatViewSet(SeedRoute.ChatViewSet):
    
    @action(methods=['post'], detail=False)
    def save_message(self, request):
        print(request.data)
        has_fields_or_400(request.data, 'message', 'user_id')
        generate_chatbot_response(request.data['message'], request.data['user_id'])
        return Response(status=status.HTTP_200_OK)