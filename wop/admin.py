from django.contrib import admin
from .models import *


admin.site.register(Wall)
admin.site.register(SlideShow)
admin.site.register(ScreenSetup)

admin.site.register(ImageRepo)

admin.site.register(Screen)
admin.site.register(Tag)

admin.site.register(Image)