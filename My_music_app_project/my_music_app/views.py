from django.shortcuts import render


def index(request):
    return render(request, 'core/home-with-profile.html')


def details_album_page(request, pk):
    return render(request, 'albums/album-details.html')


def add_album_page(request):
    return render(request, 'albums/add-album.html')


def edit_album_page(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album_page(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile_page(request):
    return render(request, 'profiles/profile-details.html')


def delete_profile_page(request):
    return render(request, 'profiles/profile-delete.html')
