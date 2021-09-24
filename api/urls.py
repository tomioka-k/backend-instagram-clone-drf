from django.conf.urls import include
from django.urls import path, include
from rest_framework import urlpatterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)

app_name = "user"
urlpatterns = [
    path('', include(router.urls),),
    path('register/', views.CreateUserView.as_view(), name="register"),
    path('myprofile', views.MyProfileListView.as_view(), name="myprofile"),
]