from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import MemorialCreateView, MemorialEditView


app_name = 'memorials'


# Memorial CRUD Operations
path(
    'memorials/create/',
    MemorialCreateView.as_view(),
    name='memorial_create',
),
path(
        'memorials/<int:pk>/edit/',
        MemorialEditView.as_view(),
        name='memorial_edit',
),
