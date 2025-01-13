from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('opcion1/', views.opcion1, name='opcion1'),
    path('opcion2/', views.opcion2, name='opcion2'),
    # path('opcion3/', views.opcion3, name='opcion3'),
    
    
    path('register/', views.crear_usuario, name='create'),
    
    
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    
]
