"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Chat(Model):
    
    TYPES = (
        ('USER', 'USER'),
        ('BOT', 'BOT'),
    )

    type = models.CharField(
        max_length=64, choices=TYPES,
        blank=False)
    message = models.TextField(blank=True)

    user = models.ForeignKey(
        'models.User', related_name='chats',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_chat'
        app_label = 'models'