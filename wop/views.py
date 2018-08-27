from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseForbidden
from django.http import HttpResponse
from .forms import *
from wop.tools.scan_repo import scan_repo
from wop.tools.next_pic import select_next_pic


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
    if request.method == 'GET':
        image_repo = get_object_or_404(ImageRepo, pk=image_repo_id)
        form = ImageRepoForm(instance=image_repo)
    elif request.method == 'POST':
        image_repo = get_object_or_404(ImageRepo, pk=image_repo_id) if image_repo_id else None
        form = ImageRepoForm(request.POST, instance=image_repo)
        form.save()
    else:
        return HttpResponseForbidden("Method not allowed")

    context = {
        'form': form,
        'image_repo': image_repo,
    }
    return render(request, 'image_repo.html', context)


def image_repo_scan(request, image_repo_id):
    if request.method != 'POST':
        return HttpResponseForbidden("Method not allowed")
    image_repo = get_object_or_404(ImageRepo, pk=image_repo_id)
    new_images = scan_repo(image_repo)
    context = {
        'image_repo': image_repo,
        'new_images': new_images,
    }
    return render(request, 'image_repo_scan.html', context)


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
    return render(request, 'screen_detail.html', context)


def config_view(request):
    return render(request, 'config.html')


def img(request, key):
    """serve a pic as is from its key"""
    i = get_object_or_404(Image, key=key)
    with open(i.path, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def image(request, image_id):
    """image detail view"""
    i = get_object_or_404(Image, pk=image_id)
    context = {
        'image': i,
    }
    return render(request, 'image_detail.html', context)


def scr(request, screen_id):
    """screen renderer"""
    screen = get_object_or_404(Screen, pk=screen_id)
    context = {
        'screen': screen
    }
    return render(request, 'screen.html', context)


def wall_list_view(request):
    context = {
        'walls': Wall.objects.all()
    }
    return render(request, 'wall_list.html', context)


def wall_detail_view(request, wall_id):
    wall = get_object_or_404(Wall, pk=wall_id)
    context = {
        'wall': wall,
    }
    return render(request, 'wall_detail.html', context)


def wall_action_view(request, wall_id):
    wall = get_object_or_404(Wall, pk=wall_id)
    status = request.GET['action'].upper()
    if status == 'PLAY':
        # stop other running walls on the same screen setup
        walls = Wall.objects.filter(status='PLAY', screen_setup=wall.screen_setup)
        for w in walls:
            w.status = 'STOP'
            w.save()
    wall.status = status
    wall.save()
    return redirect('wall_list')

