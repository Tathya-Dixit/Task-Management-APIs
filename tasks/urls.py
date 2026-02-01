from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')

urlpatterns = router.urls
