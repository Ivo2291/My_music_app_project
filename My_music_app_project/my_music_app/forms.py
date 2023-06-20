from django import forms
from My_music_app_project.my_music_app.models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileForm):
    pass


class ProfileDeleteForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_to_hidden()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Album.objects.all().delete()
        else:
            return self.instance

    def __set_fields_to_hidden(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class AlbumForm(forms.ModelForm):
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


class AlbumCreateForm(AlbumForm):
    pass


class AlbumEditForm(AlbumForm):
    pass


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_to_disable()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __set_fields_to_disable(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = True
