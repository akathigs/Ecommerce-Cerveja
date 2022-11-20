from . import views
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('products', views.makeProducts),
    path('about', views.makeAbout),
    path('login', views.makeLogin),
]