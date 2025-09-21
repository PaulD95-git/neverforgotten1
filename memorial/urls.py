from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import (
    MemorialCreateView,
    memorial_detail,
    update_name,
    update_dates,
    update_banner,
    update_quote,
    update_biography,

)


app_name = 'memorials'


urlpatterns = [

    # Memorial CRUD Operations
    path(
        'memorials/create/',
        MemorialCreateView.as_view(),
        name='memorial_create',
    ),
    path(
        'memorials/<int:pk>/',
        memorial_detail,
        name='memorial_detail',
    ),

    # User Account

    path(
        'accounts/logout/',
        LogoutView.as_view(next_page='home'),
        name='logout',
    ),

    # Memorial Media Updates
    path(
        '<int:pk>/upload-profile-picture/',
        views.upload_profile_picture,
        name='upload_profile_picture',
    ),
    path(
        'memorials/<int:pk>/update-name/',
        update_name,
        name='update_name',
    ),
    path(
        'memorials/<int:pk>/update-dates/',
        update_dates,
        name='update_dates',
    ),
    path(
        'memorials/<int:pk>/update-banner/',
        update_banner,
        name='update_banner',
    ),
    path(
        'memorials/<int:pk>/update-quote/',
        update_quote,
        name='update_quote',
    ),
    path(
        'memorials/<int:pk>/update-biography/',
        update_biography,
        name='update_biography',
    ),

    # Audio Handling
    path(
        '<int:pk>/upload-audio/',
        views.upload_audio,
        name='upload_audio',
    ),

    # Gallery Management
    path(
        'memorials/<int:pk>/upload-gallery/',
        views.upload_gallery_images,
        name='upload_gallery_images',
    ),
    path(
        '<int:memorial_id>/gallery/<int:image_id>/delete/',
        views.delete_gallery_image,
        name='delete_gallery_image',
    ),
]
