from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Item
from .forms import SignupForm, loginForm
from django.contrib.auth import login as auth_login


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

def loginPage(request):
    page = 'login'
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")
    context = {"form":form,"page":page}
    return render(request, 'core/login_register.html',context)


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'core/login_register.html',context)