from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages

from front import forms

# Create your views here.
# def home(request):
#     return render(request, 'front/home.html')


class HomeView(TemplateView):
    template_name = 'front/home.html'
    def get(self, request):
        
        return render(request, self.template_name)

class ContactView(TemplateView):
    form_class = forms.ContactForm
    template_name = 'front/contact.html'

    def get(self, request):

        contactForm = self.form_class()

        return render(request, self.template_name, { 'form': contactForm })

    def post(self, request):

        contactForm = self.form_class(request.POST)

        if contactForm.is_valid():
            contact = contactForm.save()
            messages.success(request, 'Contact saved')
            return HttpResponseRedirect('contact')

        return render(request, self.template_name, { 'form': contactForm })