from django.shortcuts import render, HttpResponse
from .models import Team, Event, HomePageContent, AboutUsPage, Forum
from accounts.models import UserPhotos
import json
from datetime import datetime

def homepage(request):
    homepg = None
    content = HomePageContent.objects.all()
    for homepag in content:
        homepg = homepag
    return render(request, 'aces_homepage.html', {'content': homepg})

def listevents(request):
    events = Event.objects.all()
    return render(request, 'eventindex.html', {'events': events})

def eventviewer(request, event_name):
    particular_event = Event.objects.filter(event_name=event_name)
    for eventobj in particular_event:
        event = eventobj
    return render(request, 'particularevent.html', {'event': event})

def listteams(request):
    teams = Team.objects.all()
    return render(request, 'teamindex.html', {'teams': teams})
    

def teamviewer(request, team_name):
    particular_team = Team.objects.filter(team_name=team_name)
    for teamobj in particular_team:
        team = teamobj
    return render(request, 'particularteam.html', {'team': team})

def aboutus(request):
    about = ""
    aboutqueries = AboutUsPage.objects.all()
    for aboutobj in aboutqueries:
        about = aboutobj
    return render(request, 'aboutus.html', {'about': about})

def discussions(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            username = request.user.username
        msg = json.loads(request.body)
        print()
        msg = msg['msg']
        Forum.objects.create(name=username, msg=msg)
        now = datetime.now()
        return HttpResponse(json.dumps({'name': username, 'msg': msg, 'date': str(now)}), content_type='application/json')
    else:
        discussionobj = Forum.objects.all()
        return render(request, 'forum.html', {'all_discussions': discussionobj})
