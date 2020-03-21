from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import Adbform

from .models import Adb
from .models import Tag

def index(request):
    adb = Adb.objects.all()
    context = {'adb': adb}
    return render(request, 'adboard/index.html', context)

class AdbCreateView(CreateView):
    template_name = 'adboard/add.html'
    form_class = Adbform
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

def account(request):
    pass

