from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.decorators import role_required


def index_page(request):
    """Главная страница. Возвращает простой ответ 'Ok' для проверки работы сервера."""
    return HttpResponse("Ok")


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
    return render(request, "create_publication.html")


@role_required('write')  # Требует права на запись (роль 'write')
def remove_publication(request):
    """Страница удаления публикации."""
    return render(request, "remove_publication.html")


@role_required('moderator')  # Требует прав модератора
def create_organization(request):
    """Страница создания организации."""
    return render(request, "create_organization.html")


@role_required('moderator')  # Требует прав модератора
def remove_organization(request):
    """Страница удаления организации."""
    return render(request, "remove_organizations.html")


@role_required('moderator')  # Требует прав модератора
def register_writer(request):
    """Страница регистрации писателя."""
    return render(request, "register_writer.html")


@role_required('moderator')  # Требует прав модератора
def delete_writer(request):
    """Страница удаления писателя."""
    return render(request, "delete_writer.html")


def login(request):
    """Авторизация пользователя. Сохраняет user.id в сессию и перенаправляет на главную."""
    request.session['user_id'] = user.id  # Предполагается, что user определен ранее
    return redirect('home')


def logout(request):
    """Выход пользователя. Удаляет user_id из сессии и перенаправляет на главную."""
    del request.session['user_id']
    return redirect('home')
