"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Chat
from app.models import User
from app.models import File

class Admin:
    # pylint: disable=R0914,R0915
    @staticmethod
    def register():
        
        class ChatResource(resources.ModelResource):
            pass

        class ChatAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ChatResource
            class Meta:
                model = Chat
                fields = (
                    'id',
                    'created_at',
                    'type',
                    'message',
                    'user',
                )
        
        class UserResource(resources.ModelResource):
            pass

        class UserAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = UserResource
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                )
        
        class FileResource(resources.ModelResource):
            pass

        class FileAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = FileResource
            class Meta:
                model = File
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'url',
                    'size'
                )
        admin.site.register(Chat, ChatAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)