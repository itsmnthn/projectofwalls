from django.forms import ModelForm
from walls.models import Wallpapers

class WallpapersForm(ModelForm):
    class Meta:
        model = Wallpapers
        fields = [
            'title',
            'image',
            'category',
            'tags',
            'location',
            'description',
            'uploader',
            'likes',
            'downloads',
            'views',
            'slug',
            'active',
        ]