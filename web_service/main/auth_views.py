from django.shortcuts import render, redirect
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"login: {username} {password}")
        # user = external_db.get_user(username, password)
        user = {
            "id": 123,
            "user_role": "write"
        }

        if user:
            request.session['user_id'] = user['id']
            request.session['user_role'] = user['user_role']
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверные учетные данные'})

    return render(request, 'login.html')


def logout_view(request):
    request.session.flush()
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"login: {username} {password}")
        # role = 'guest'  # По умолчанию регистрируем как гостя
        try:
            # user_id = external_db.create_user(username, password, role)
            request.session['user_id'] = 123
            request.session['user_role'] = "moderator"
            return redirect('home')
        except Exception as e:
            return render(request, 'register.html', {'error': str(e)})

    return render(request, 'register.html')
