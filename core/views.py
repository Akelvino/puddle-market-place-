from django.shortcuts import render, redirect
from .models import Category, Item

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    context = {
        "items":items,
        "categories":categories
    }
    return render(request, 'core/index.html', context)



def contact(request):
    return render(request, 'core/contact.html')