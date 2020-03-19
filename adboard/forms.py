from django.forms import ModelForm

from .models import Adb

class Adbform(ModelForm):
    class Meta:
        model = Adb
        fields = ('title', 'content', 'tag')