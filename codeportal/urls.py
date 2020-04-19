from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('submitsolution/', views.code_edit_and_submit, name="problemscreen"),
    path('contact/', views.contact, name='contact'),
]