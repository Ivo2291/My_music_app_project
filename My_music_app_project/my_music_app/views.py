from My_music_app_project.my_music_app.forms import ProfileCreateForm
from My_music_app_project.my_music_app.models import Profile
from django.shortcuts import render, redirect


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return redirect('add profile')

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


def add_profile_page(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == "GET":
        form = ProfileCreateForm()

    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'core/home-no-profile.html', context)


def delete_profile_page(request):
    return render(request, 'profiles/profile-delete.html')
