#Personal.views

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Welcome to Index of Personal</h1>')
    return render(request,'personal/index.html')

def contact(request):
    return render(request, 'personal/contact.html',{'content':['address is bla bbla ','phone is bla bla '],'email':['email is bla bla ','gmail is gmail ']})
