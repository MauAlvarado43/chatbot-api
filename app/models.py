"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_chat():
    import seed.models.chat as SeedModel
    return SeedModel.Chat

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Chat = get_chat()
User = get_user()
File = get_file()