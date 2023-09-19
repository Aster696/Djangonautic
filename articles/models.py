from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    # add in thumnail
    # add in author later

    def __str__(self):
        return self.title
    
    def snippets(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        else:
            return self.body