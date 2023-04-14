from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("Welcome to DJANGO Class")
def eMobilis(request):
    return HttpResponse("Emobilis Mobile Institute")
def Microsoft(request):
    return HttpResponse("The best work happens when you mind improving other peoples lives")
def Fact(request):
    return HttpResponse("Everyone needs a coach." "Lousy people think they cannot lose")
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about us.html')