from django.urls import path
from main import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('/user/login', views.login, name='login'),
    path('/user/logout', views.logout, name='logout'),
]
