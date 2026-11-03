from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')