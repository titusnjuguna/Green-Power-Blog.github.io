"""Young_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from Users import views as User_view 
from django.contrib.auth import views as auth_view
from Subscribers.views import subscribe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',User_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='Users/login.html'),name='login'),
    path('logout/', auth_view.LoginView.as_view(template_name='Users/logout.html'),name='logout'),
    path('Profile/', User_view.Profile, name='Profile'),
    path('subscribe/confirm', subscribe, name='Subscribe-name'),
    path('',include('Blog.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
