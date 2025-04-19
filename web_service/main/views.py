from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.decorators import role_required
from django.core.files.storage import default_storage


def view_index(request):
    """
    Главная страница. Возвращает простой ответ 'Ok' для проверки работы сервера
    """
    return render(request, "index.html")


def search_posts(request):
    """Страница поиска публикаций. Рендерит шаблон searching_page.html."""
    return render(request, "searching_page.html")


def view_post(request, post_id):
    """Страница публикации. Передает данные в шаблон publication.html."""
    print(post_id)
    # data = dict()  # Заглушка для будущих данных
    return render(request, "publication.html")


@role_required('write')
def create_post(request):
    """Страница создания публикации."""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        main_image_url = request.FILES.get('logo')

    return render(request, "create_publication.html")


@role_required('moderator')
def delete_post(request, post_id):
    """Удаление поста"""
    print(post_id)
    return render(request, "remove_organizations.html")


@role_required('write')
def update_publication(request):
    """Страница обновления публикации."""
    if request.method == 'POST':
        post_id = request.POST.get('id')
    return render(request, "remove_publication.html")


@role_required('moderator')
def create_organization(request):
    """Создание организации"""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "remove_organizations.html")


@role_required('moderator')
def delete_organization(request, organization_id):
    """Удаление организации"""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "remove_organizations.html")


@role_required('moderator')
def view_organizations(request):
    """Просмотр всех доступных организаций"""
    return render(request, "remove_organizations.html")


@role_required('moderator')
def create_writer(request):
    """Создание писателя"""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "register_writer.html")


@role_required('moderator')
def delete_writer(request):
    """Удаления писателя"""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "delete_writer.html")
