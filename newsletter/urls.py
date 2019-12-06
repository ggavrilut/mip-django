from django.urls import path
from .views import NewsletterView, DeleteNewsletterView, NewsletterAjax

urlpatterns = [
    path('', NewsletterView.as_view(), name='newsletter'),
    path('ajax', NewsletterAjax.as_view(), name='newsletter_ajax'),
    path('delete/<str:email>', DeleteNewsletterView.as_view(), name='newsletter_delete')
]
