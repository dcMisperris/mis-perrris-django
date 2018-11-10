from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def adoptar(request):
    return render(request,'adoptar.html',{})
