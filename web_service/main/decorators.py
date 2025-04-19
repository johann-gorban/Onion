def role_required(role_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if 'user_id' not in request.session:
                return redirect('/login/')

            user_id = request.session['user_id']
            user = get_user_from_your_db(user_id)  # Ваша функция для получения пользователя

            if user.role != role_name:  # Проверяем роль
                return HttpResponse("Доступ запрещен", status=403)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
