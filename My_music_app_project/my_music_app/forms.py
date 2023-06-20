from django import forms
from My_music_app_project.my_music_app.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'image_URL': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }
