from django.urls import path
from main import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
]
