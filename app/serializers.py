"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_chat_serializer():
    import seed.serializers.chat as SeedSerializer
    return SeedSerializer.ChatSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

ChatSerializer = get_chat_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()