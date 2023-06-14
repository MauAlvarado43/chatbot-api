"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.chat
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    saveChat = seed.mutations.chat \
        .SaveChatMutation.Field()
    setChat = seed.mutations.chat \
        .SetChatMutation.Field()
    deleteChat = seed.mutations.chat \
        .DeleteChatMutation.Field()
    saveUser = seed.mutations.user \
        .SaveUserMutation.Field()
    setUser = seed.mutations.user \
        .SetUserMutation.Field()
    deleteUser = seed.mutations.user \
        .DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)