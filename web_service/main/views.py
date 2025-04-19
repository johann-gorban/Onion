from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.decorators import role_required


def index_page(request):
    return HttpResponse("Ok")


def searching_publications(request):
    return render(request, "searching_page.html")


def organizations_list(request):
    return render(request, "organizations_list.html")


def publication(request):
    # когда-нибудь будут данные
    data = dict()
    return render(request, "publication.html")


@role_required('write')
def create_publication(request):
    return render(request, "create_publication.html")


@role_required('write')
def remove_publication(request):
    return render(request, "remove_publication.html")


@role_required('moderator')
def create_organization(request):
    return render(request, "create_organization.html")


@role_required('moderator')
def remove_organization(request):
    return render(request, "remove_organizations.html")


@role_required('moderator')
def register_writer(request):
    return render(request, "register_writer.html")


@role_required('moderator')
def delete_writer(request):
    return render(request, "delete_writer.html")


def login(request):
    request.session['user_id'] = user.id
    return redirect('home')


def logout(request):
    del request.session['user_id']
    return redirect('home')
