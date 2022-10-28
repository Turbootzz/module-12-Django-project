from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime
from django.utils import timezone

# Create your views here.


def home(request):
    anime = Anime.objects

    #print(anime.values())
    return render(request, 'anime/anime.html', {'anime': anime})


def detail(request, anime_id):
    ani = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'anime/detail.html', {'ani': ani})


def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            ani = Anime()
            ani.title = request.POST['title']
            ani.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
               ani.url = request.POST['url']
            else:
               ani.url = 'http://' + request.POST['url']
               ani.icon = request.FILES['icon']
               ani.image = request.FILES['image']
               ani.pub_date = timezone.datetime.now()
               ani.hunter = request.user
               ani.save()
            return redirect('/anime/' + str(ani.id))
        else:
            return render(request, 'anime/toevoegen.html', {'error': 'niet alle velden zijn ingevuld.'})
    else:
        return render(request, 'anime/toevoegen.html')
