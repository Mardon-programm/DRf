from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.views import UserAPI, UserRegisterAPI

router = DefaultRouter
router.register(r'user', UserAPI, basename='user')
router.register(r'user_create', UserRegisterAPI, basename='user_create')

urlpattterns = [

    
]
urlpattterns += router.urls