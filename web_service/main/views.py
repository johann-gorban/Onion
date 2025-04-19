from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.decorators import role_required
from django.core.files.storage import default_storage


def index_page(request):
    """Главная страница. Возвращает простой ответ 'Ok' для проверки работы сервера."""
    return render(request, "index.html")


def searching_publications(request):
    """Страница поиска публикаций. Рендерит шаблон searching_page.html."""
    return render(request, "searching_page.html")


def organizations_list(request):
    """Страница со списком организаций. Рендерит шаблон organizations_list.html."""
    return render(request, "organizations_list.html")


def publication(request):
    """Страница публикации. Передает данные в шаблон publication.html."""
    data = dict()  # Заглушка для будущих данных
    return render(request, "publication.html")


@role_required('write')  # Требует права на запись (роль 'write')
def create_publication(request):
    """Страница создания публикации."""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        main_image_url = request.FILES.get('logo')

    return render(request, "create_publication.html")

@role_required('write')  # Требует права на запись (роль 'write')
def remove_publication(request):
    """Страница удаления публикации."""
    if request.method == 'POST':
        post_id = request.POST.get('id')
    return render(request, "remove_publication.html")

@role_required('write')  # Требует права на запись (роль 'write')
def update_publication(request):
    """Страница обновления публикации."""
    if request.method == 'POST':
        post_id = request.POST.get('id')
    return render(request, "remove_publication.html")

@role_required('moderator')  # Требует прав модератора
def create_organization(request):
    """Страница создания организации."""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image_url = request.FILES['logo']
        print(image_url)
        # path = default_storage.save('uploads/' + image_url.name, image_url)
    return render(request, "create_organization.html")


@role_required('moderator')  # Требует прав модератора
def remove_organization(request):
    """Страница удаления организации."""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "remove_organizations.html")


@role_required('moderator')  # Требует прав модератора
def create_writer(request):
    """Страница регистрации писателя."""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "register_writer.html")


@role_required('moderator')  # Требует прав модератора
def delete_writer(request):
    """Страница удаления писателя."""
    if request.method == 'POST':
        user_id = request.POST.get('id')
    return render(request, "delete_writer.html")
