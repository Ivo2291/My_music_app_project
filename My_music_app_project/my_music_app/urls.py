from django.urls import path, include

from My_music_app_project.my_music_app.views import index, add_album_page, details_album_page, edit_album_page, \
    delete_album_page, details_profile_page, delete_profile_page, add_profile_page

urlpatterns = (
    path('', index, name='index'),
    path('album/', include(
        [
            path('details/<int:pk>/', details_album_page, name='album details'),
            path('add/', add_album_page, name='add album'),
            path('edit/<int:pk>/', edit_album_page, name='edit album'),
            path('delete/<int:pk>/', delete_album_page, name='delete album'),
        ]
    )),

    path('profile/', include(
        [
            path('details/', details_profile_page, name='profile details'),
            path('add/', add_profile_page, name='add profile'),
            path('delete/', delete_profile_page, name='delete profile')
        ]
    )),
)
