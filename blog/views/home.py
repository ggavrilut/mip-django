from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Entry

class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request):
        # existentEntries = Entry.objects.filter(slug__exact='first-post')
        # print('start iteration')
        # for entry in existentEntries:
        #     print(entry)
        # print('end iteration')

        newEntry = Entry()
        newEntry.title = 'First post'
        newEntry.body = 'Content'
        newEntry.save()
        return render(request, self.template_name, { 'blog_entry': newEntry })