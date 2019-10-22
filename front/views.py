from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return render(request, 'front/home.html')


class HomeView(TemplateView):
    template_name = 'front/home.html'

class ContactView(TemplateView):
    template_name = 'front/contact.html'