from django.shortcuts import render, redirect
from . import models


# def sign_up (request):
#     if request.method == 'POST':
#         form = 
#     return render (request, 'registration/sign_up.html', {})








# will be using django.contrib.auth.urls to renfer login page, forbiden and 404 pages


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Welcome back')
#                 return redirect('home')
#             else:
#                 messages.info(request, 'username or password is incorrect! ')

#     return render(request, "registration/login.html", )

