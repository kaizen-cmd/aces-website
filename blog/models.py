from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.db.models.signals import post_save
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from accounts.models import UserPhotos as User
from django.utils.timezone import now

class BlogPosts(models.Model):
    title = models.TextField()
    date = models.DateField(default=now)
    picture = models.ImageField(upload_to="pics/")
    body = RichTextField()
    footer = RichTextField()
    prevblogtitle = models.TextField()
    nextblogtitle = models.TextField()

def mass_mailer(sender, **kwargs):
    if kwargs['created']:
        p = User.objects.all()
        msg1 = '<a href="https://codestrike.pythonanywhere.com/blog/post/{}"> Codestrike|Blog </a>'.format(kwargs['instance'].title)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("codestrike20@gmail.com", "khalidown@2020")
        msg = MIMEMultipart()
        msg['From'] = "codestrike20@gmail.com"
        msg['Subject'] = "Code_Strike Information"
        body = "New Blog has been posted. Check it out now"
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(msg1, 'html'))
        for i in p:
            sleep(1)
            print(i)
            msg['To'] = i.email
            text = msg.as_string()
            try:
                server.sendmail("codestrike20@gmail.com", i.email, text)
            except:
                continue
        server.close()

post_save.connect(mass_mailer, sender=BlogPosts)
