from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
import re
from django.core.exceptions import ValidationError
from django.utils.timezone import now

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

class Problem_statements(models.Model):
    problem_name = RichTextField()
    problem = RichTextField()
    example = RichTextField()
    input_format = RichTextField()
    output_format = RichTextField()
    test_case = RichTextField()
    date_added = models.DateTimeField(default=now)
    show = models.BooleanField()
    def __str__(self):
        p = remove_html_tags(self.problem_name)
        return '{}'.format(p)

class Submission(models.Model):
    contestant = models.TextField(max_length=100)
    probstatement = models.TextField(max_length=100)
    submissions = models.TextField()
    output = models.TextField()
    check = models.TextField(max_length=20)
    date = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.contestant)

class Homepage(models.Model):
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 instance of %s." % model.__name__)

    description = RichTextField()
    rules = RichTextField()


