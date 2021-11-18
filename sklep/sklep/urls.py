from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from api.views import MensClothesViewSets, WomensClothesViewSets
from api.views import odziezMeska,odziezDamska, index



router = routers.DefaultRouter()
router.register('odziezmeska', MensClothesViewSets)
router.register('odziezdamska', WomensClothesViewSets)

nested_router = NestedDefaultRouter(router, 'odziezmeska', lookup='odziezmeska')
nested_router.register('typubraniam', MensClothesViewSets, basename='typubraniam')

nested_router = NestedDefaultRouter(router, 'odziezdamska', lookup='odziezdamska')
nested_router = NestedDefaultRouter('typubraniak', WomensClothesViewSets, basename='typubraniak')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(router.get_urls())),
    path('api/', include(nested_router.get_urls())),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
