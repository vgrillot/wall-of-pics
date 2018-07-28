from django.db import models


class ScreenSetup(models.Model):
    """Set of screens"""
    name = models.CharField(max_length=20)


class Screen(models.Model):
    """Physical screen description
       Even it's more a description of each different browser window
    """
    name = models.CharField(max_length=20)
    screen_setup = models.ForeignKey(ScreenSetup, on_delete=models.CASCADE)
    # screen information
    ratio = models.FloatField()  # X/Y


class ImageRepo(models.Model):
    """Physical and local directoy to store image"""
    name = models.CharField(max_length=40)
    path = models.CharField(ml=500)


class SlideShow(models.Model):
    """Define what to display, images source, effects, tempo, ..."""
    name = models.CharField(max_length=40)
    repos = models.ManyToManyField(ImageRepo)


class Tag(models.Model):
    """Tag information about images"""
    name = models.CharField(10)


class Image(models.Model):
    """Information about an image"""
    path = models.CharField(max_length=500, null=False)
    repo = models.ForeignKey(ImageRepo, on_delete=models.CASCADE)
    # image information
    # analysed : True when the file will be anlysed to extract meta
    analysed = models.BooleanField(default=False)
    width = models.IntegerField()
    height = models.IntegerField()
    ratio = models.FloatField()  # X/Y
    monochrome = models.BooleanField(default=False)  # True if the image is monochrome
    b_w = models.BooleanField(default=False)  # True of the image is (almost) black and white
    # file information
    file_date = models.DateTimeField()
    scan_date = models.DateTimeField()
    #  descriptive informations
    tags = models.ManyToManyField(Tag)


class Wall(models.Model):
    """A wall is the top entry level, kind of a project,
       Will use ScreenSetup to display a SlideShow
    """
    name = models.CharField(max_length=50)
    screen_setup = models.ForeignKey(ScreenSetup, on_delete=models.CASCADE)
    slide_show = models.ForeignKey(SlideShow, on_delete=models.CASCADE)


