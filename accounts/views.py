from django.shortcuts import render, redirect
from accounts.models import UserPhotos as User
from django.contrib import auth
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_auth = auth.authenticate(username=username, password=password)
        if user_auth is not None:
            auth.login(request, user_auth)
            return redirect('/')
        else:
            messages.info(request, "Wrong username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.info(request, "Username or email already exists")
            return redirect('register')
        else:
            try:
                User.objects.create_user(username=username, password=password, email=email, first_name=name.split(" ")[0], last_name=name.split(" ")[1])
            except:
                messages.info(request, "Improper format of name entered")
                return redirect('register')
            email_sender(email, "Hello, {}\nWe are glad you chose our platform to enhance your coding skills. We look forward to your participation. Keep striking keep coding !".format(name.split(" ")[0]), "Welcome to Code_Strike")
            return redirect('login')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
