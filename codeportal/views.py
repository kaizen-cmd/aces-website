from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import Problem_statements, Submission, Homepage
import subprocess, os
from time import sleep
from datetime import datetime
import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def home(request):
    hp = Homepage.objects.all()
    sendhp = None
    for i in hp:
        sendhp = i
    return render(request, 'home.html', {'hp': sendhp})

def contact(request):
    return render(request, 'contact.html')

def code_edit_and_submit(request):
    res = None
    compiled = None
    if request.method == "POST":
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        code =json.loads(request.body)
        psname = code['pname']
        psname.strip(" ")
        if code['code'] == "":
            res = "No code written"
        if "import os" in code['code'] or "import subprocess" in code['code'] or "filesystem" in code['code']:
            res = "These commands are not allowed to be used here."
        else:
            if code['cmd'] == "submit":
                sub = Submission()
                sub.contestant = username
                sub.probstatement = psname
                sub.submissions = code['code']
            code_file = open("code.txt", "w+")
            code_file.write(code['code'])
            code_file.close()
            base = os.path.splitext('code.txt')[0]
            if code['lang'] == "python":
                os.rename('code.txt', base + ".py")
                sleep(1)
                p = subprocess.Popen(["python", "code.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                sleep(5)
                p.kill()
                out, err = p.communicate()
                error = err.decode('utf-8')
                compiled = out.decode('utf-8')
                os.remove("code.py")
                if error == "" :
                    res = compiled
                    if code['cmd'] == "submit":
                        psobj = Problem_statements.objects.filter(show=True)
                        for i in psobj:
                            ps = i
                        test = ps.test_case
                        test = remove_html_tags(test)
                        res = res.strip()
                        sub.output = res
                        if res == test:
                            sub.check = "Correct"
                        else:
                            sub.check = "Wrong"
                else:
                    res = error
                    if code['cmd'] == "submit":
                        sub.check = "Compilation Error"


            if code['lang'] == "c":
                os.rename('code.txt', base + ".c")
                sleep(1)
                p = subprocess.Popen(["gcc", "code.c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                sleep(5)
                p.kill()
                noout, err = p.communicate()
                print(err)
                try:
                    q = subprocess.Popen(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    sleep(4)
                    q.kill()
                    out, noerror = q.communicate()
                except Exception:
                    pass
                error = err.decode('utf-8')
                print(error)
                try:
                    compiled = out.decode('utf-8')
                except Exception:
                    pass
                os.remove("code.c")
                try:
                    os.remove("a.out")
                except Exception:
                    pass
                if error == "" :
                    res = compiled
                    if code['cmd'] == "submit":
                        psobj = Problem_statements.objects.filter(show=True)
                        for i in psobj:
                            ps = i
                        test = ps.test_case
                        test = remove_html_tags(test)
                        res = res.strip()
                        sub.output = res
                        if res == test:
                            sub.check = "Correct"
                        else:
                            sub.check = "Wrong"
                else:
                    res = error
                    if code['cmd'] == "submit":
                        sub.check = "Compilation Error"


            if code['lang'] == "cpp":
                os.rename('code.txt', base + ".cpp")
                sleep(1)
                p = subprocess.Popen(["g++", "code.cpp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                sleep(5)
                p.kill()
                noout, err = p.communicate()
                print(err)
                try:
                    q = subprocess.Popen(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    sleep(4)
                    q.kill()
                    out, noerror = q.communicate()
                except Exception:
                    pass
                error = err.decode('utf-8')
                print(error)
                try:
                    compiled = out.decode('utf-8')
                except Exception:
                    pass
                os.remove("code.cpp")
                try:
                    os.remove("a.out")
                except Exception:
                    pass
                if error == "" :
                    res = compiled
                    if code['cmd'] == "submit":
                        psobj = Problem_statements.objects.filter(show=True)
                        for i in psobj:
                            ps = i
                        test = ps.test_case
                        test = remove_html_tags(test)
                        res = res.strip()
                        sub.output = res
                        if res == test:
                            sub.check = "Correct"
                        else:
                            sub.check = "Wrong"
                else:
                    res = error
                    if code['cmd'] == "submit":
                        sub.check = "Compilation Error"



        if code['cmd'] == "submit":
            sub.date = datetime.now()
            sub.save()
        return HttpResponse(json.dumps({'res': res}), content_type="application/json")
    else:
        ps = Problem_statements.objects.filter(show=True)
        probobj = None
        for i in ps:
            probobj = i
        return render(request, 'psandeditor.html', {'ps': probobj})
