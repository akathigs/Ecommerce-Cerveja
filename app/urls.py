from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.makeIndex),
    path('products', views.ProdctListView.as_view()),
    path('about/', views.makeAbout),
    path('login', views.makeLogin),
    path('register', views.makeRegister, name='cadastro'),
    path('contact', views.makeContact)
]