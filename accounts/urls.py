from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('success/', views.success_view, name='success'),
    path('logout/', LogoutView.as_view(), name='logout'),
]