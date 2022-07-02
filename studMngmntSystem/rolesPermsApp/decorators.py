from django.shortcuts import redirect
from django.http import HttpResponse


# Ref:  https://www.youtube.com/watch?v=eBsc65jTKvw


# stop unauthenticated users from viewing the admin & student page build with the 'rolesPermsApp' app.
# here the "view_func" is the actual function on which this decorator will be set to.
def stop_unauthenticated_users(view_func):
    def wrapper_func(request, *args, **kwargs):
        # -------------
        # Build the logic here, if needed, then redirect the user from inside that logic,
        # then lastly, return the "view_func"
        # -------------
        if not request.user.is_authenticated:
            return redirect('authApp:userLogin')
        else:
            return view_func(request, *args, **kwargs)  # let the user to get returned to the original function
    return wrapper_func

# To make the decorators more dynamic, create groups



def allow_admins_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            return HttpResponse('You are not allowed to view this admin page!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allow_staff_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponse('You are not allowed to view this staff page!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allow_student_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_active:
            return HttpResponse('You are not allowed to view this student page!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
