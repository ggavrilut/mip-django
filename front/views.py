from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'front/home.html'
    def get(self, request):
        
        return render(request, self.template_name)