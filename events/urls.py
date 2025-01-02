from django.urls import path # type: ignore
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Fixed
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Fixed
    path('event-list/', views.event_list, name='event_list'),  # Define the event_list URL pattern
    path('create/', views.create_event, name='create_event'),
]


