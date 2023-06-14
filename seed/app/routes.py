"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_chat_viewset():
    import routes.chats as ExtendViewSet
    return ExtendViewSet.ChatViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

ChatViewSet = get_chat_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()