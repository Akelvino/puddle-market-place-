from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Item
from .forms import SignupForm, loginForm, NewItem
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


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

@login_required
def newItem(request):
    form = NewItem()
    if request.method == 'POST':
        form = NewItem(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit = False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    context = {
        "form":form
    }
    return render(request, 'core/item_form.html', context)

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by = request.user)
    context = {
        "items":items
    }
    return render(request, 'core/dashboard.html', context)