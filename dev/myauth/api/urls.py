from django.urls import path, include
from rest_framework import routers
from .users_authentication import *


router = routers.DefaultRouter()


urlpatterns=[
    
    path('', include(router.urls)),
    path('mid_level_user_register/', mid_level_user_register.as_view()),
    path('low_level_user_register/', low_level_user_register.as_view()),
    path('high_level_user_register/', high_level_user_register.as_view()),
    path('login/', LoginView.as_view(), name='login'),

]