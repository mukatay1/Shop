from django.urls import path

from .views import (logout_user, auth)

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', logout_user, name='logout'),

]
