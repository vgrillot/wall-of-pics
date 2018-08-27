from django.db import models
import os


class ScreenSetup(models.Model):
    """Set of screens"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Screen(models.Model):
    """Physical screen description
       Even it's more a description of each different browser window
    """
    name = models.CharField(max_length=20)
    # key = models.CharField(max_length=20, null=True, unique=True, default="UNSET")
    screen_setup = models.ForeignKey(ScreenSetup, on_delete=models.CASCADE)
    # screen information
    ratio = models.FloatField()  # X/Y

    def __str__(self):
        return self.name


class ImageRepo(models.Model):
    """Physical and local directory to store image"""
    name = models.CharField(max_length=40)
    path = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SlideShow(models.Model):
    """Define what to display, images source, effects, tempo, ..."""
    name = models.CharField(max_length=40)
    repos = models.ManyToManyField(ImageRepo)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag information about images"""
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Image(models.Model):
    """Information about an image"""
    path = models.CharField(max_length=500, null=False)
    repo = models.ForeignKey(ImageRepo, on_delete=models.CASCADE)
    key = models.CharField(max_length=20, null=False, unique=True, default="UNSET")
    # image information
    # analysed : True when the file will be analysed to extract meta
    analysed = models.BooleanField(default=False)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    ratio = models.FloatField(null=True)  # X/Y
    monochrome = models.BooleanField(default=False)  # True if the image is monochrome
    b_w = models.BooleanField(default=False)  # True of the image is (almost) black and white
    # file information
    file_date = models.DateTimeField(null=True)
    scan_date = models.DateTimeField()
    #  descriptive information
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.path

    def filename(self):
        return os.path.basename(self.path)


class Wall(models.Model):
    """A wall is the top entry level, kind of a project,
       Will use ScreenSetup to display a SlideShow
    """
    name = models.CharField(max_length=50)
    screen_setup = models.ForeignKey(ScreenSetup, on_delete=models.CASCADE)
    slide_show = models.ForeignKey(SlideShow, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
