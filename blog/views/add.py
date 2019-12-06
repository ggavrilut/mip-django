from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from ..models import Entry, Tag
from ..forms import EntryForm
from django.forms import modelformset_factory
from django.shortcuts import render

# class AddView(CreateView):
#     model = Entry
#     fields = ['title', 'teaser', 'body', 'tags']

from django.views.generic import TemplateView
from ..models import Entry

class AddView(CreateView):
    template_name = 'blog/add.html'
    
    
    def get(self, request, *args, **kwargs):
        entryForm = EntryForm()
        tagsFormset = modelformset_factory(Tag, fields=('name',))
        return render(request, self.template_name, { 'entryForm': entryForm, 'tagsFormset': tagsFormset })

    def post(self, request, *args, **kwargs):
        print(request.POST)
        entryForm = EntryForm(request.POST)
        if(entryForm.is_valid()):
            entryForm.save()
        tagsFormset = modelformset_factory(Tag, fields=('name',), request.POST)
        if(tagsFormset.is_valid()):
            for tagForm in tagsFormset:
                tagForm.save()
        
        return HttpResponse('submit');