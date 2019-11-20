from django.urls import path
from .views import NewsletterView, DeleteNewsletterView

urlpatterns = [
    path('', NewsletterView.as_view(), name='newsletter'),
    path('delete/<str:email>', DeleteNewsletterView.as_view(), name='newsletter_delete')
]
