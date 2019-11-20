from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class NewsletterView(TemplateView):
    template_name = 'newsletter/index.html'