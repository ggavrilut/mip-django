from django.db import models
from django.utils.text import slugify

class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, )
    body = models.TextField()
    teaser = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        # existentEntries = Entry.objects.filter(slug=self.slug)
        # print('start iteration')
        # for entry in existentEntries:
        #     print(entry)
        # print('end iteration')


        # super(Entry, self).save(*args, **kwargs)
    


class Tag(models.Model):
    name = models.CharField

    def __str__(self):
        return self.name
    