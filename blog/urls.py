from django.urls import path
from blog.views.home import HomeView
from blog.views.add import AddView

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('add', AddView.as_view(), name='blog_add')
]
