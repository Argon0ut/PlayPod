import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Album, Track
from .serializer import TrackSerializer, AlbumSerializer
import requests
# Create your views here.


@api_view(['GET'])
def get_all_tunes(request):
    tunes = Track.objects.all()
    serializer = TrackSerializer(tunes, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_tune_by_id(request, pk):
    tune = Track.objects.get(pk=pk)
    serializer = TrackSerializer(tune, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_all_albums(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tracks_by_album(request, pk):
    tracks = Track.objects.filter(album_id=pk)
    serializer = TrackSerializer(tracks, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def search_external_tracks(request):
    query = request.GET.get('item')
    if not query:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    url = f"https://itunes.apple.com/search?term={query}&media=music"
    response = requests.get(url)
    data = response.json()

    data_results = []
    print(json.dumps(data, indent=2))
    for item in data.get('results', []):
        data_results.append({
            'title': item.get('trackName'),
            'artist': item.get('artistName'),
            'album': item.get('collectionName'),
            'cover': item.get('artworkUrl100'),
            'audio_file': item.get('previewUrl'),
            'genre': item.get('primaryGenreName'),
            'external': True
        })
    return Response(data_results)


def base_page(request):
    return render(request, 'layouts/base.html')

def album_page(request):
    return render(request, 'home/albums.html')

def album_tracks_page(request, pk):
    album = Album.objects.get(pk=pk)
    context = {'album':album,
               'album_id': pk
               }
    return render(request, 'home/albums_track_list.html', context)

def catalog_page(request):
    return render(request, 'home/catalog.html')

def favorite_page(request):
    return render(request, 'home/favorites_list.html')

def track_player(request, pk):
    track = Track.objects.get(pk=pk)
    context = {'track': track,
               'track_id': pk
               }
    return render(request, 'home/track_player.html', context)

def search_tunes(request):
    return render(request, 'home/tune_search.html')

def external_tune_player(request):
    title = request.GET.get('title')
    artist = request.GET.get('artist')
    context = {'title': title,
               'artist': artist,}
    return render(request, 'home/external_tune_player.html', context)
