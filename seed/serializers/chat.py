"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Chat
from app.models import User

class ChatSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Chat
        fields = (
            'id',
            'created_at',
            'hash',
            'type',
            'message',
            'user_id',  
        )