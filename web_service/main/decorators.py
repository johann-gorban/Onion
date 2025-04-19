from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def role_required(*roles):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            # user = external_db.get_user_by_id(request.session['user_id'])
            if request.session['user_role'] not in roles:
                return HttpResponseForbidden("Доступ запрещен")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
