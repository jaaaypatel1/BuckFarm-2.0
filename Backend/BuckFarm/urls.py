from django.contrib import admin
from django.urls import path
from farm import views  # Make sure to import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.products, name='home'),  # Add this line for the root URL
    path('products/', views.products, name='products'),  # Existing products path
]
