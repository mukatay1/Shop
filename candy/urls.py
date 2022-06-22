from django.urls import path
from .views import (HomePage,
                    CandyDetail,
                    CandySearch,
                    )

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('candy/<slug:candy_slug>/', CandyDetail.as_view(), name='candy_detail'),
    path('search/', CandySearch.as_view(), name='candy_search')
]
