from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import ContactForm



class ContactView(TemplateView):
    form_class = ContactForm
    template_name = 'contact/index.html'

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