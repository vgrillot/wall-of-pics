from django.forms import ModelForm
from .models import *


class ImageRepoForm(ModelForm):
    class Meta:
        model = ImageRepo
        fields = ['name', 'path']
