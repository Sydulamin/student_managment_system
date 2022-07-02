from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def userReg(request):
    # empty form
    form = UserRegForm()

    if request.method == 'POST':
        print(request.POST['first_name'])
        print(request.POST['last_name'])
        print(request.POST['username'])
        print(request.POST['email'])
        print(request.POST['password'])


    context = {
        'form': form,
    }
    return render(request, 'authentication/reg.html', context)





def userLogin(request):
    if request.method == 'POST':
        print('Login Post Request!')
        # print('Username:', request.POST['username'])
        # print('Password:', request.POST['passwordInput'])

        user = authenticate(request, username=request.POST['username'], password=request.POST['passwordInput'])

        # user = User.objects.get(username=request.POST['username'], password=request.POST['passwordInput'])

        if user is not None:
            login(request, user)
            print('Authenticated User:', user)
            print('Staff User:', user.is_staff)
            print('Admin User:', user.is_superuser)
            print('Active User:', user.is_active)

            # business logic to route the user to their appropriate pages based on the user-permissions
            # superuser
            if user.is_superuser:
                return redirect('rolesPermsApp:adminPage')
            # staff user
            if user.is_superuser == False and user.is_staff == True:
                return redirect('rolesPermsApp:staffPage')
            # normal user/ student
            if user.is_superuser == False and user.is_staff == False and user.is_active == True:
                # The changes is done here ######################################
                print("Username (user-login func):", user.id)

                return redirect(reverse('rolesPermsApp:studPage', kwargs={ 'id':user.id }))
                # The changes is done here ######################################
        else:
            print("User is not found!")
            messages.info(request, "User login failed!")
            return render(request, 'authentication/login.html')

            # for i in dir(user):
            #     print(i)
            # return redirect('rolesPermsApp:commonPage')

    return render(request, 'authentication/login.html')



def userLogout(request):
    logout(request)
    return redirect('authApp:userLogin')
    pass
