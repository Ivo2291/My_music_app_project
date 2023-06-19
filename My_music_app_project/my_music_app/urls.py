"""
• http://localhost:8000/ - home page
• http://localhost:8000/album/add/ - add album page
• http://localhost:8000/album/details/<id>/ - album details page
• http://localhost:8000/album/edit/<id>/ - edit album page
• http://localhost:8000/album/delete/<id>/ - delete album page
• http://localhost:8000/profile/details/ - profile details page
• http://localhost:8000/profile/delete/ - delete profile page

"""
from My_music_app_project.my_music_app.views import index, add_album_page, details_album_page, edit_album_page, \
    delete_album_page, details_profile_page, delete_profile_page
from django.urls import path, include

urlpatterns = (
    path('', index, name='index'),
    path('album/', include(
        [
            path('details/<int:id>/', details_album_page, name='album details'),
            path('add/', add_album_page, name='add album'),
            path('edit/<int:id>/', edit_album_page, name='edit album'),
            path('delete/<int:id>/', delete_album_page, name='delete album'),
        ]
    )),

    path('profile/', include(
        [
            path('details/', details_profile_page, name='profile details'),
            path('delete/', delete_profile_page, name='delete profile')
        ]
    )),
)
