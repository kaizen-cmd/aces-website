from django.contrib import admin
from . import models
from django.urls import path
from accounts.models import UserPhotos as User
from django.shortcuts import HttpResponseRedirect
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

admin.site.site_header = "ACES Admin Dashboard"
admin.site.site_title = "Code Strike"
admin.site.index_title = "ACES"

def email_sender(to, message, subject):
    msg = MIMEMultipart()
    msg['From'] = "codestrike20@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("codestrike20@gmail.com", "khalidown@2020")
    text = msg.as_string()
    server.sendmail("codestrike20@gmail.com", to, text)
    server.close()

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('contestant', 'probstatement', 'check', 'date')
    list_filter = ('probstatement', 'contestant')
    change_list_template = 'admin/submission/submission_change_list.html'
    readonly_fields = ['contestant', 'probstatement', 'check', 'date', 'submissions', 'output']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sendemails/', self.mass_mail),
        ]
        return custom_urls + urls

    def mass_mail(self, request):
        if request.method == "POST":
            addrs = request.POST['emails']
            p = User.objects.all()
            print(p)
            if addrs == "all":
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("codestrike20@gmail.com", "khalidown@2020")
                msg = MIMEMultipart()
                msg['From'] = "codestrike20@gmail.com"
                msg['Subject'] = "Code_Strike Information"
                body = "Next Code Strike on Monday 6:00 pm ! Participate in large numbers."
                msg.attach(MIMEText(body, 'plain'))
                for i in p:
                    sleep(1)
                    print(i)
                    msg['To'] = i.email
                    text = msg.as_string()
                    try:
                        server.sendmail("codestrike20@gmail.com", i.email, text)
                    except:
                        pass
                server.close()
            elif "," not in addrs:
                print("here")
                p = User.objects.filter(username=addrs).values('email')
                em = p.first()
                to = em['email']
                try:
                    email_sender(to, "Congratulations on winning CODE_STRIKE this week. As winners, your name will be put up on ACES's Instagram account and our blog circulated in all the  groups. For this purpose, we will need some details from you.\n1. Full name\n2. Class (mention your academic year)\n3. Your picture\n4. Your Instagram handle (if any)\n\nWe are looking forward to your participation in the upcoming weeks.\n\nThank You,\nTeam Code_Strike", "Code_Strike Rankings")
                except:
                    pass
            elif "," in addrs:
                addrs = addrs.split(", ")
                for user in addrs:
                    p = User.objects.filter(username=user).values('email')
                    em = p.first()
                    to = em['email']
                    try:
                        email_sender(to, "Congratulations on winning CODE_STRIKE this week. As winners, your name will be put up on ACES's Instagram account and our blog circulated in all the  groups. For this purpose, we will need some details from you.\n1. Full name\n2. Class (mention your academic year)\n3. Your picture\n4. Your Instagram handle (if any)\n\nWe are looking forward to your participation in the upcoming weeks.\n\nThank You,\nTeam Code_Strike", "Code_Strike Rankings")
                    except:
                        pass

            return HttpResponseRedirect('../')

class HomepageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
                return False
        else:
                return True


admin.site.register(models.Problem_statements)
admin.site.register(models.Submission, SubmissionAdmin)
admin.site.register(models.Homepage, HomepageAdmin)
