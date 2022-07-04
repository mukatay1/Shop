from django.urls import path

from .views import (logout_user,
                    auth,
                    newsletter
                    )

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', logout_user, name='logout'),
    path('newsletter/', newsletter, name='newsletter')
]
