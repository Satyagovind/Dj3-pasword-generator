from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
     return render(request , 'generator/Home.html')

def password(request):

     elements=list('abcdfghijklmnopqrstuvwxyz')
     

     
     lenght=int(request.GET.get('length',12))
     if request.GET.get('uppercase','ABCDEFGHIJKLMNOPQRST'):
          elements.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('digits',32459):
          elements.extend(list('0123456789'))
     if request.GET.get('specialchar','!$%^#'):
          elements.extend(list('!@#$%^&*()_+":>?/|}{<,.[]=-'))

     
     passgen = ''
     for i in range(lenght):
          passgen += random.choice(elements)


     return render(request ,'generator/password.html',{'password':passgen})

def about(request):
     return render(request,'generator/about.html')



def raja(request):
     return HttpResponse('<h2>This is <em>Satya Govind</em>, The admin of the page<h2/>')