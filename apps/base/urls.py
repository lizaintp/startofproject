from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.base import views
from apps.users.views import UserAPI

router = DefaultRouter()
router.register('news_arrivals', views.NewArrivalsApi,'news_arrivals'),
router.register('users', UserAPI, 'api_users')


urlpatterns = router.urls