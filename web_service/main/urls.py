from django.urls import path
from main import views
from main.auth_views import (
    login, logout
)

urlpatterns = [
    path('', views.view_index, name='home'),
    path('posts/search/', views.search_posts, name='search_posts'),
    path('posts/<str:post_id>/', views.view_post, name='view_post'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/delete/<str:post_id>/', views.delete_post, name='delete_post'),

    path('organizations/create/', views.create_organization,
         name='create_organization'),
    path('organizations/delete/<str:organization_id>/',
         views.delete_organization, name='delete_organization'),
    path('organizations/', views.view_organizations, name='organizations_list'),

    path('writer/create/', views.create_writer, name="create_writer"),
    path('writer/delete/', views.delete_writer, name="delete_writer"),
    path('login/<str:user_role>/', login, name='login'),

    path('logout/', logout, name='logout'),
]
