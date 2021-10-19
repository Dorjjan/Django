from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import OdziezMeskaViewSets, OdziezDamskaViewSets,TypUbraniaMViewSets, TypUbraniaKViewSets
from api.views import index

router = routers.DefaultRouter()
router.register(r'users', OdziezMeskaViewSets)
router.register(r'user', OdziezDamskaViewSets)
router.register(r'user', TypUbraniaMViewSets)
router.register(r'user', TypUbraniaKViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
