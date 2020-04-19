from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import UserPhotos
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class Event(models.Model):
    event_name = models.TextField(max_length=100)
    event_desc = RichTextField()
    event_pic = models.ImageField(upload_to='pics/')
    event_contact = models.ManyToManyField(UserPhotos)
    event_link = models.TextField()
    def __str__(self):
        return self.event_name

class Team(models.Model):
    team_name = models.TextField(max_length=100)
    team_members = models.ManyToManyField(UserPhotos)
    team_desc = RichTextField()
    def __str__(self):
        return self.team_name

class Forum(models.Model):
    name = models.TextField()
    msg = models.TextField(max_length=500)
    date = models.DateTimeField(default=now)
    def __str__(self):
        return self.name

class HomePageContent(models.Model):
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 instance of %s." % model.__name__)
    
    def __str__(self):
        return "HomePageContent"

    pagecontent = RichTextField()
    ment_disp = models.ManyToManyField(UserPhotos)
    event_disp = models.ManyToManyField(Event)

class AboutUsPage(models.Model):
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 instance of %s." % model.__name__)
    def __str__(self):
        return "AboutUsPageContent"
    vision = RichTextField()
    mission = RichTextField()
    






