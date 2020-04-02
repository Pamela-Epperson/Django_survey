from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# Create your views here.

def index(request):
    if 'count_att' not in request.session:
        request.session['count_att']=1
    return render(request, 'index.html')

def process_randword(request):
    request.session['randword'] = get_random_string(length=14)
    print(request.session['randword'])
    request.session['count_att'] += 1
    print(request.session['count_att'])
    return redirect('/')
    







