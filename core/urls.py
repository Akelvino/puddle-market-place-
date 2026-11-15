from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path("", views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('new-item', views.newItem, name='new-item'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.delete, name='delete-item'),
    path('Edit/<int:pk>/', views.editItems, name='edit-item'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
