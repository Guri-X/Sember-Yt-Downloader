from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
import youtube_dl
from django.contrib import messages

class Home(TemplateView):
    template_name = "index.html"


class About(TemplateView):
    template_name = "about.html"

class Contact(TemplateView):
    template_name = "contact.html"

def Download(request):
    if request.method == 'POST':
        video_url = request.POST['link']
        vp = request.POST['folder']
        if video_url:
            ydl_opts = {
                'format': 'best',
                'outtmpl': vp + '%(title)s.%(ext)s',
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('Home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('Home')
    return redirect('Home')

class DownloadC(View):
    def post(self, request):
        video_url = request.POST['link']
        if video_url:
            ydl_opts = {'outtmp1': '/home/guri/Downloads'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('Home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('Home')
        return redirect('Home')
