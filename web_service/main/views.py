from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return HttpResponse("Ok")


def main_page(request):
    return render(request, "main_page.html")


def searching_publications(request):
    return render(request, "searching_page.html")


def organizations_list(request):
    return render(request, "organizations_list.html")


def publication(request):
    # когда-нибудь будут данные
    data = dict()
    return render(request, "publication.html")


def create_publication(request):
    return render(request, "create_publication.html")


def remove_publication(request):
    return render(request, "remove_publication.html")


def create_organization(request):
    return render(request, "create_organization.html")


def register_writer(request):
    return render(request, "register_writer.html")


def delete_writer(request):
    return render(request, "delete_writer.html")
