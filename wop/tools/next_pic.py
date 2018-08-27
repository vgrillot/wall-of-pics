"""
search the next pic to display for a wall
"""

from django.utils.timezone import make_aware
from django.db.models import F

from wop import models
from random import randint
from datetime import datetime


def select_next_pic(wall: models.Wall, screen: models.Screen):
    """return the next pic"""
    repos = wall.slide_show.repos.all()
    index = randint(0, repos.count() - 1)
    repo: models.ImageRepo = repos[index]
    print(repo.name)
    # index = randint(0, repo.image_set.count() - 1)
    if screen.ratio > 1:
        filter = 'ratio__gte'
    else:
        filter = 'ratio__lte'


    # **{filter:value} tip: https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
    images = repo.image_set \
        .filter(**{filter: 1.0}) \
        .order_by(F('last_view').asc(nulls_first=True))

    print(images.count())
    print(images.query)

    if images:
        image = images[0]
        image.last_view = make_aware(datetime.now())
        image.view_count += 1
        image.save()
        return image
    else:
        return None  # might because the active repo is empty
