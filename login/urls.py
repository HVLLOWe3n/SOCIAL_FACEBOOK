from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.login_function, name='login'),
    path('login_success/', views.get_login_success, name='success')
]
