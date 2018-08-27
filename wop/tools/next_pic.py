"""
search the next pic to display for a wall
"""

from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import make_aware
from django.db.models import F
from django.utils.timezone import make_aware

from wop import models
from random import randint
from datetime import datetime


def select_next_pic(wall : models.Wall):
    """return the next pic"""
    repos = wall.slide_show.repos.all()
    # TODO: choose repo proportionnaly from number of imgages...
    index = randint(0, repos.count() - 1)
    repo: models.ImageRepo = repos[index]
    # index = randint(0, repo.image_set.count() - 1)
    images = repo.image_set.all().order_by(F('last_view').asc(nulls_first=True))
    image = images[0]
    image.last_view = make_aware(datetime.now())
    image.view_count += 1
    image.save()
    return image

