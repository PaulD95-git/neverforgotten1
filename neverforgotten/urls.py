from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from memorial import views

handler404 = views.custom_page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),



    path('', include('memorial.urls')),

    path('plans/', include('plans.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
