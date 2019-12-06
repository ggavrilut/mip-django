from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .form import NewsletterForm
from .models import Newsletter
from django.contrib import messages
from django.db.models import Count
from .service import ContactService

# Create your views here.

class NewsletterView(FormView):
    template_name = 'newsletter/index.html'
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # newsletters = Newsletter.objects.all()
        # newsletters = Newsletter.objects.filter(email__startswith="gabriel")
        # newsletters = Newsletter.objects.values('email').annotate(subscribers=Count('email')).order_by('-email')
        newsletters = Newsletter.objects.values('email').annotate(subscribers=Count('email')).order_by('email')
        context['newsletters'] = newsletters
        return context
        

    def form_valid(self, form):
        print(form.cleaned_data['email'])
        contactService = ContactService()
        contactService.saveNewsletter(form.cleaned_data['email'])
        messages.add_message(self.request, messages.SUCCESS, 'Thank you.')
        return super().form_valid(form)


class DeleteNewsletterView(View):

    def get(self, request, *args, **kwargs):

        email = kwargs['email']
        emailNewsletters = Newsletter.objects.filter(email__exact=email)
        emailNewslettersCount = emailNewsletters.count()
        print(emailNewslettersCount)
        if(emailNewslettersCount > 0):
            for emailNewsletter in emailNewsletters:
                emailNewsletter.delete()
            messages.add_message(self.request, messages.INFO, 'Deleted.')
        else: 
            messages.add_message(self.request, messages.WARNING, 'Subscriber does not exist.')

        return redirect('newsletter')
    

class NewsletterAjax(View):

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        print(request.POST)
        contactService = ContactService()
        contactService.saveNewsletter(request.POST['email'])
        
        return JsonResponse({'message': 'success'})