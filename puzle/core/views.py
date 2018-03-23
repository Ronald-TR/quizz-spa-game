from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def root(request):
    return render(request, 'core/home.html')

def statement(request):
    if request.method == 'POST':
        statement = 'insert into bote values("nabunda")'
        if request.POST.get('sql') == statement:
            return HttpResponse('<h3 style="text-align:center">wonderfull job! Await for more phases</h3>')
    return redirect('/')
    