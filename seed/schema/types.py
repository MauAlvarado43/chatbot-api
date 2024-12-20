"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

# pylint: disable=C0302
import graphene
import secrets
import math
from graphene import ObjectType
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType
from app.models import Chat as ChatModel
from app.models import User as UserModel
from app.models import File as FileModel
from seed.util.query_util import sql_alike_q

class Chat(DjangoObjectType):
    id = graphene.Int(description="Chat primary key")
    class Meta:
        model = ChatModel
        
    def resolve_id(self, info):
        return self.pk

class ChatPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    chats = DjangoListField(Chat)

class ChatCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    id = graphene.Int(description="User primary key")
    class Meta:
        model = UserModel
        exclude = ('password',)
        
    def resolve_id(self, info):
        return self.pk

class UserPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    users = DjangoListField(User)

class UserCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class FilePagination(ObjectType):
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    files = DjangoListField(File)

class FileCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

def resolve_list(model, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        res = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
    else:
        res = model.objects.all()
    if "orderBy" in kwargs:
        orders = kwargs["orderBy"].split(",")
        for order in orders:
            res = res.order_by(order)
    if "start" in kwargs and "end" not in kwargs:
        res = res[kwargs["start"]:]
    if "end" in kwargs and "start" not in kwargs:
        res = res[:kwargs["end"]]
    if "start" in kwargs and "end" in kwargs:
        res = res[kwargs["start"]:kwargs["end"]]
    res = model.filter_permissions(res, model.permission_filters(user))
    return res

def resolve_pagination(model, model_name, pagination_type, info, **kwargs):
    total_count = len(resolve_list(model, info, **kwargs))
    total_pages = math.ceil(total_count / kwargs["pageSize"])
    kwargs["start"] = (kwargs["pageNum"] - 1) * kwargs["pageSize"]
    kwargs["end"] = (kwargs["pageNum"]) * kwargs["pageSize"]
    page = resolve_list(model, info, **kwargs)

    return pagination_type(**{
       "id": int(''.join(secrets.choice("0123456789") for i in range(9))),
       "pageNum": kwargs["pageNum"],
       "pageSize": kwargs["pageSize"],
       "totalPages": total_pages,
       "totalCount": total_count,
       model_name: page
    })

def resolve_count(model, count_type, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        query = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
    else:
        query = model.objects.all()
    query = model.filter_permissions(query, model.permission_filters(user))

    return count_type(
        id=int(''.join(secrets.choice("0123456789") for i in range(9))),
        count=len(query))

# pylint: disable=R0904
class Query(object):
    
    chats = graphene.List(
        Chat, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    chatPagination = graphene.Field(
        ChatPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    chatCount = graphene.Field(
        ChatCount, query=graphene.String())
    chat = graphene.Field(
        Chat, id=graphene.Int(required=True))
    users = graphene.List(
        User, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    userPagination = graphene.Field(
        UserPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    userCount = graphene.Field(
        UserCount, query=graphene.String())
    user = graphene.Field(
        User, id=graphene.Int(required=True))
    files = graphene.List(
        File, query=graphene.String(), orderBy=graphene.String(), limit=graphene.Int())
    filePagination = graphene.Field(
        FilePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    file = graphene.Field(File, id=graphene.Int(required=True))
    fileCount = graphene.Field(FileCount, query=graphene.String())

    # pylint: disable=C0103
    def resolve_chats(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(ChatModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_chatPagination(self, info, **kwargs):
        return resolve_pagination(
            ChatModel, 'chats',
            ChatPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_chatCount(self, info, **kwargs):
        return resolve_count(
          ChatModel, ChatCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_chat(self, info, id):
        user = info.context.user
        return ChatModel.filter_permissions(
            ChatModel.objects,
            ChatModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_users(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(UserModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userPagination(self, info, **kwargs):
        return resolve_pagination(
            UserModel, 'users',
            UserPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userCount(self, info, **kwargs):
        return resolve_count(
          UserModel, UserCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_user(self, info, id):
        user = info.context.user
        return UserModel.filter_permissions(
            UserModel.objects,
            UserModel.permission_filters(user)).get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(FileModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_filePagination(self, info, **kwargs):
        return resolve_pagination(FileModel, 'files', FilePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_fileCount(self, info, **kwargs):
        return resolve_count(FileModel, FileCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_file(self, info, id):
        user = info.context.user
        return FileModel.filter_permissions(
            FileModel.objects, FileModel.permission_filters(user)).get(pk=id)
    pass