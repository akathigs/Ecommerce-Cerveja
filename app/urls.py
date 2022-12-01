from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.makeIndex),
    path('products', views.makeProducts),
    path('about', views.makeAbout),
    path('login', views.makeLogin),
    path('register', views.makeRegister),
    path('contact', views.makeContact)
]