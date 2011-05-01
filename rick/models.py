from django.db import models

# Create your models here.

class RickrollStory(models.Model):
    fake_title = models.CharField(max_length=128)
    fake_image = models.URLField(null=True, blank=True)
    url = models.URLField(help_text="Default behaviour opens url in an iframe", default="http://www.youtube.com/embed/oHg5SJYRHA0")
    views = models.IntegerField(editable=False, default=0)
    
    greeting_to_victim = models.TextField(blank=True)
    
    def increase_views(self, amount=1):
        self.views += amount
        self.save()
        return ""