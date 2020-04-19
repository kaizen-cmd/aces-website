from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('events/', views.listevents, name="events"),
    path('events/<slug:event_name>/', views.eventviewer, name="particular-event"),
    path('teams/', views.listteams, name='teams'),
    path('teams/<slug:team_name>/', views.teamviewer, name="particular-team"),
    path('aboutus/', views.aboutus, name="about-us"),
    path('discussion/', views.discussions, name="forum"),
]