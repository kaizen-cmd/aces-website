from django.test import TestCase
import subprocess

p = subprocess.Popen(["g++", "test.cpp"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate()
p = subprocess.Popen(["a.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                    
out, err = p.communicate()
