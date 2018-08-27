"""
tool unit to scan repository and update database
"""
from functools import reduce

from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import make_aware
from wop import models
import PIL.Image
import PIL.ImageStat


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

            infos = image_analysis(image)  # TODO:for test purposes

        if j > 5:
            break # TODO: for testing, do only 5 scan (quicker, repeatable without db delete)
    return new_images


def image_analysis(image:models.Image):
    """read file information"""
    file = PIL.Image.open(image.path)

    image.width = file.size[0]
    image.height = file.size[1]
    image.ratio = image.width / image.height
    image.b_w = isblack(file)
    image.analysed = True
    image.save()


def isblack(file):
    """check if filename is a black & white photo
    """
    # from https://www.programcreek.com/python/example/92040/PIL.ImageStat.Stat
    MONOCHROMATIC_MAX_VARIANCE = 0.005
    COLOR = 1000
    MAYBE_COLOR = 200
    v = PIL.ImageStat.Stat(file).var
    is_monochromatic = reduce(lambda x, y: x and y < MONOCHROMATIC_MAX_VARIANCE, v, True)
    if is_monochromatic:
        return True
    else:
        if len(v) == 3:
            maxmin = abs(max(v) - min(v))
            if maxmin > COLOR:
                return False
            elif maxmin > MAYBE_COLOR:
                return False
            else:
                return True
        elif len(v)==1:
            return True
        else:
            #don't know
            return False