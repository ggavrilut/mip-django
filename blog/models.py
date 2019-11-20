from django.db import models
from django.utils.text import slugify

class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    body = models.TextField()
    teaser = models.TextField()

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        existentEntriesCount = Entry.objects.filter(slug__startswith=self.slug).count()
        if(existentEntriesCount > 0):
            self.slug = self.slug + '-' + str(existentEntriesCount)
            
        super().save(*args, **kwargs)
    


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    