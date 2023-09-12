from django.shortcuts import redirect
from django.contrib import messages


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.success(request, "To view this page, please log in.")
            return redirect('home')
    return wrapper
