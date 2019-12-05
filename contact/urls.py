from django.urls import path
from .views import ContactView, contactV1, ContactFormView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('v1/', contactV1, name='contact_v1'),
    path('v2/', ContactFormView.as_view(), name='contact_v2')
]
