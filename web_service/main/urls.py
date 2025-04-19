from django.urls import path
from main import views
from main.auth_views import (
    login_view, logout_view, register_view
)

urlpatterns = [
    path('', views.index_page, name='home'),
    path(
        'posts/search/',
        views.searching_publications,
        name='searching_publications'
    ),
    path('organizations/', views.organizations_list, name='organizations_list'),

    path('posts/<str:id>/', views.publication, name='publication'),
    path('posts/create/', views.create_publication, name='create_publication'),
    path('posts/delete/<str:id>/', views.remove_publication, name='remove_publication'),
    path('posts/update/<str:id>', views.update_publication, name="update_publication"),

    path('organizations/create/', views.create_organization,
         name='create_organization'),
    path('organizations/delete/<str:id>/',
         views.remove_organization, name='remove_organization'),

    path('writer/create/', views.create_writer, name="create_writer"),
    path('writer/delete/', views.delete_writer, name="delete_writer"),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
