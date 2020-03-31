from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method != "POST":
        return redirect("/")
    print(request.POST['your_name'])
    print(request.POST['location'])
    print(request.POST['language'])
    print(request.POST['comment'])
    context = {
        'your_name':request.POST['your_name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'comment':request.POST['comment'],
    }
    return render(request, "results.html", context)