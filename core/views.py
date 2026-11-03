from django.shortcuts import render, redirect, get_object_or_404
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

def detail(request, pk):
    items = get_object_or_404(Item, id=pk)
    related_items = Item.objects.filter(category = items.category, is_sold=False).exclude(id=pk)[0:3]
    context = {"items":items,"related_items":related_items}
    return render(request, 'core/details.html', context)

def contact(request):
    return render(request, 'core/contact.html')