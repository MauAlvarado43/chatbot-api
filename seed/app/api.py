"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from seed.app.routes import ChatViewSet
from seed.app.routes import UserViewSet
from seed.app.routes import FileView

router = DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]