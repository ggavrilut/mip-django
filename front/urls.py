from django.urls import path
from front.views import HomeView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('contact', ContactView.as_view(), name='contact')
]
