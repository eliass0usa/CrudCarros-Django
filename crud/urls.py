from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    
    # LOGIN E LOGOUT
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    # DEFAULT
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]