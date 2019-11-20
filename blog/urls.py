from django.urls import path
from blog.views.home import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home')
]
