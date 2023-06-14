"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Chat
from app.models import User
from seed.schema.types import Chat as ChatType

class SaveChatMutation(graphene.Mutation):
    
    chat = graphene.Field(ChatType)
    
    class Arguments:
        type = graphene.String(required=True)
        message = graphene.String(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        chat = {}
        if "type" in kwargs:
            chat["type"] = kwargs["type"]
        if "message" in kwargs:
            chat["message"] = kwargs["message"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            chat["user"] = user
        chat = \
            Chat.objects.create(**chat)
        chat.save()
    
        return SaveChatMutation(
            chat=chat)

class SetChatMutation(graphene.Mutation):
    
    chat = graphene.Field(ChatType)
    
    class Arguments:
        id = graphene.Int(required=True)
        type = graphene.String(required=False)
        message = graphene.String(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        chat = Chat.filter_permissions(
            Chat.objects,
            Chat.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "type" in kwargs:
            chat.type = kwargs["type"]
        if "message" in kwargs:
            chat.message = kwargs["message"]
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            chat.user = user
        chat.save()
    
        return SetChatMutation(
            chat=chat)

class DeleteChatMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        chat_id = kwargs["id"]
        chat = Chat.objects.get(pk=kwargs["id"])
        chat.delete()
        return DeleteChatMutation(
            id=chat_id)