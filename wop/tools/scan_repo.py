"""
tool unit to scan repository and update database
"""
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import make_aware
from wop import models


#!!180826:Creation

import os
import glob
from datetime import datetime


def scan_repo(image_repo:models.ImageRepo):
    """
    scan a local repository and update database
    :return:
    """
    # TODO: scan the scan status in db...
    new_images = []
    j = 0
    for i, f in enumerate(glob.glob(os.path.join(image_repo.path, '*.*'))):
        print(f)
        try:
            _ = models.Image.objects.get(repo=image_repo, path=f)
        except ObjectDoesNotExist:
            j += 1
            image = models.Image()
            image.repo = image_repo
            image.path = f
            image.file_date = make_aware(datetime.now())  # TODO:read real file date
            image.scan_date = make_aware(datetime.now())
            image.key = hex(abs(hash(image.path)))[2:]  # get unique identifier
            image.save()
            new_images.append(image)
        if j > 5:
            break # TODO: for testing, do only 5 scan (quicker, repeatable without db delete)
    return new_images
