from rest_framework import routers
from .views import CustomerViewSet,ProductViewSet
from django.urls import path, include

app_name = "ecomapp"

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)
router.register('product', ProductViewSet)

urlpatterns = [path('', include(router.urls))]