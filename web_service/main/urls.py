from django.urls import path
from main import views
from main.auth_views import (
    login, logout
)

urlpatterns = [
    path('', views.index_page, name='home'),
    path('posts/search/', views.searching_posts, name='searching_posts'),

    path('posts/<str:id>/', views.view_posts, name='view_posts'),
    path('posts/create/', views.create_posts, name='create_posts'),
    path('posts/delete/<str:id>/', views.remove_posts, name='remove_posts'),

    path('organizations/create/', views.create_organization,
         name='create_organization'),
    path('organizations/delete/<str:id>/',
         views.remove_organization, name='remove_organization'),
    path('organizations/', views.organizations_list, name='organizations_list'),

    path('writer/create/', views.create_writer, name="create_writer"),
    path('writer/delete/', views.delete_writer, name="delete_writer"),
    path('login/<str:user_role>/', login, name='login'),

    path('logout/', logout, name='logout'),
]
