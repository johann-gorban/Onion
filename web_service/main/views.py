from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return HttpResponse("Ok")

def login(request):
    request.session['user_id'] = user.id
    return redirect('home')

def logout(request):
    del request.session['user_id']
    return redirect('home')
