# joy/views.py
from django.shortcuts import render
from .models import Leadership, Program, News, Event, GalleryImage
from django.http import HttpResponseRedirect
from .forms import *

def homepage(request):
    leadership = Leadership.objects.all()
    programs = Program.objects.all()
    news = News.objects.order_by('-date')[:3]
    events = Event.objects.order_by('-date')[:3]
    images = GalleryImage.objects.all()

    return render(request, 'joy/homepage.html', {
        'leadership': leadership,
        'programs': programs,
        'news': news,
        'events': events,
        'images':images
    })

def admissions(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'joy/admissions.html', {'submitted': True})
    else:
        form = AdmissionForm()
    return render(request, 'joy/admissions.html', {'form': form})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'joy/gallery.html', {'images': images})

def contact(request):
    return render(request, 'joy/contact.html')

def academic_page(request):
    return render(request, 'joy/academic_page.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'joy/contact.html', {'submitted': True})
    else:
        form = ContactForm()
    return render(request, 'joy/contact.html', {'form': form})
