from django.shortcuts import render, get_object_or_404
from .models import *


def screen_setup_list_view(request):
    context = {
        'screen_setups': ScreenSetup.objects.all()
    }
    return render(request, 'screen_setup_list.html', context)


def repo_list_view(request):
    context = {
        'image_repos': ImageRepo.objects.all()
    }
    return render(request, 'image_repo_list.html', context)


def image_repo_detail_view(request, image_repo_id):
    image_repo = get_object_or_404(ImageRepo, pk=image_repo_id)
    context = {
        'image_repo': image_repo
    }
    return render(request, 'image_repo.html', context)


def screen_setup_detail_view(request, screen_setup_id):
    ss = get_object_or_404(ScreenSetup, pk=screen_setup_id)
    context = {
        'ss': ss
    }
    return render(request, 'screen_setup.html', context)


def screen_detail_view(request, screen_id):
    s = get_object_or_404(Screen, pk=screen_id)
    context = {
        's': s
    }
    return render(request, 'screen.html', context)


def config_view(request):
    return render(request, 'config.html')

