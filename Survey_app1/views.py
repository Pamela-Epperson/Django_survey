from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method != "POST":
        return redirect("/")
    request.session["your_name"] = request.POST['your_name']
    request.session["location"] = request.POST['location']
    request.session["language"] = request.POST['language']
    request.session["comment"] = request.POST['comment']
    return redirect(f'/results')

def results(request):    
    return render(request, "results.html")

def clear_session(request):
    request.session.flush()
    return redirect("/")