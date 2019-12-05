from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact


class ContactView(TemplateView):
    form_class = ContactForm
    template_name = 'contact/index.html'

    def get(self, request):
        contactForm = self.form_class()
        return render(request, self.template_name, { 'form': contactForm })

    def post(self, request):
        contactForm = self.form_class(request.POST, request.FILES)
        if contactForm.is_valid():
            contact = contactForm.save()
            messages.success(request, 'Contact saved')
            return HttpResponseRedirect(reverse_lazy('contact'))

        return render(request, self.template_name, { 'form': contactForm })


def contactV1(request):
    if(request.method == 'POST'):
        # save data from request to form
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact saved')
            return redirect(reverse_lazy('contact_v1')) # reverse will give error
    else: 
        form = ContactForm()
    return render(request, 'contact/v1.html', { 'form': form })


class ContactFormView(FormView): 
    template_name = 'contact/v2.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_v2')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Contact saved')
        return super().form_valid(form)
