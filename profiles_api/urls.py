from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router =DefaultRouter()
# router.register('Hello-ViewSet',views.HelloViewSet, basename='Hello-ViewSet')
router.register('profile', views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns =   [
    # path('hello/',views.HelloAPIView.as_view()),
    path('login/',views.UserLoginView.as_view()),
    path('',include(router.urls)),
]