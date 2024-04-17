from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def welcome(request):
    data = {'current_time': datetime.now(),
            'posts': Post.objects.all(),
            'num_posts': Post.objects.count()}
    return render(request, 'demo_web/welcome.html', data)


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, f'Welcome to our blog, {username}')
        return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
