from django.contrib import admin
from django.urls import path, include
from core.views import CustomerViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
