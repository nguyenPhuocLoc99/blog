"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demo_web.views import welcome, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('posts/', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', signup, name='signup'),
]

'''
- The urls provided by django.contrib.auth.urls:
accounts/login/  [name='login']
accounts/logout/  [name='logout']
accounts/password_change/  [name='password_change']
accounts/password_change/done/  [name='password_change_done']
accounts/password_reset/  [name='password_reset']
accounts/password_reset/done/  [name='password_reset_done']
accounts/reset/<uidb64>/<token>/  [name='password_reset_confirm']
accounts/reset/done/  [name='password_reset_complete']

- These urls need registration/login.html
'''
