from django.urls import path
from front.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage')
]
