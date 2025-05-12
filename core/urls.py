"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_page, name='base_page'),


    path('api/tracks/', views.get_all_tunes, name='get_tunes'),
    path('catalog/', views.catalog_page, name='catalog_page'),

    path('api/tracks/<int:pk>/', views.get_tune_by_id, name='get_tune_by_id'),
    path('player/<int:pk>/', views.track_player, name='track_player'),


    path('api/albums/', views.get_all_albums, name='get_albums'),
    path('albums/', views.album_page, name='album_page'),


    path('api/albums/<int:pk>/tracks/', views.get_tracks_by_album, name='get_tracks_by_album'),
    path('albums/<int:pk>/', views.album_tracks_page, name='album_tracks_page'),


    path('favorites/', views.favorite_page, name='favorite_page'),


    path('api/search/external/', views.search_external_tracks, name='search_external_tracks'),
    path('search/', views.search_tunes, name='search_tunes'),

    path('external/tune/player/', views.external_tune_player, name='external_tune_player'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
