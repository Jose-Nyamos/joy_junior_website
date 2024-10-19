# main/admin.py
from django.contrib import admin
from .models import Leadership, Program, News, Event, GalleryImage, Admission

admin.site.register(Leadership)
admin.site.register(Program)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(GalleryImage)
admin.site.register(Admission)
