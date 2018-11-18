from django.contrib.auth.models import User
from django.shortcuts import (Http404, HttpResponse, HttpResponseRedirect,
                              redirect, render)
from django.utils import timezone

from .forms import WallpapersForm
from .models import Categories, Wallpapers, Feedback, TeamMembers


def home(request):
    featured = Wallpapers.objects.all().order_by('id')[:6]
    latest = Wallpapers.objects.all().order_by('-created_at')[:6]
    popular = Wallpapers.objects.all().order_by('-downloads')[:6]
    return render(
        request, 'user/home.html',
        {
            'featured': featured,
            'latest': latest,
            'popular': popular
        }
    )


def download(request):
    if request.method == 'POST':
        wallpaper = Wallpapers.objects.get(slug=request.POST['slug'])
        wallpaper.downloads = wallpaper.downloads + 1
        wallpaper.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def like(request):
    if request.method == 'POST':
        wallpaper = Wallpapers.objects.get(slug=request.POST['slug'])
        wallpaper.likes = wallpaper.likes + 1
        wallpaper.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def categories(request):
    return render(request, 'user/home.html')


def register(request):

    return render(request, 'user/register.html')


def about(request):
    team = TeamMembers.objects.all()
    return render(request, 'user/about.html', {'members':team,'totalmember':int(12/len(team))})


def contact_us(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.name = request.POST['name']
        feedback.email = request.POST['email']
        feedback.description = request.POST['feedback']
        feedback.modified_at = timezone.datetime.now()
        try:
            feedback.save()
            return render(request, 'user/contact_us.html', {'success': True})
        except:
            return render(request, 'user/contact_us.html', {'failed': True})
    else:
        return render(request, 'user/contact_us.html')


def reset_password(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'user/reset_password.html')


def wallpaper(request, category, slug):
    wallpaper = Wallpapers.objects.get(
        category=Categories.objects.get(title=category), slug=slug)
    wallpaper.views = wallpaper.views + 1
    wallpaper.save()
    return render(request, 'user/wallpaper.html', {'wallpaper': wallpaper})

# def wallpaper(request):
#     return redirect('home')


def wallpaper_upload(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        # User can sign up
        # request.POST = request.POST.copy()
        # request.POST.update(
        #     {'uploader': User.objects.get(username=request.POST['uploader']),
        #     'category': Categories.objects.get(title=request.POST['category'])
        #     }
        #     )
        wall = Wallpapers()
        wall.title = request.POST['title']
        wall.category = Categories.objects.get(title=request.POST['category'])
        wall.image = request.FILES['wallpaper']

        # wall.uploader = User.objects.get(username=request.POST['uploader'])
        wall.uploader = request.user
        wall.description = request.POST['description']
        wall.tags = request.POST['tags']
        wall.modified_at = timezone.datetime.now()

        wall.save()
        wallpaper = Wallpapers.objects.get(
            title=request.POST['title'])
        return render(request, 'user/wallpaper.html', {'wallpaper': wallpaper})

        # if wall.is_valid():
        #     return render(request, 'user/upload_wallpaper.html', {"error": "Please enter valid data"})
        # else:
        #     return render(request, 'user/upload_wallpaper.html', {"error": wall.errors})
    else:
        return render(request, 'user/upload_wallpaper.html')


def profile(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/profile.html', {'wallpapers': walls})


def category(request, cat_name):
    wallpapers = Wallpapers.objects.filter(
        category=Categories.objects.get(title=cat_name)).order_by('-created_at')
    return render(request, 'user/category.html', {'category': cat_name, 'wallpapers': wallpapers})


def tag(request, tag):
    wallpapers = Wallpapers.objects.filter(tags__icontains=tag).order_by('-created_at')
    return render(request, 'user/category.html', {'category': tag, 'wallpapers': wallpapers})


def search(request):
    term = request.GET.get('search_nav')
    wallpapers = Wallpapers.objects.filter(
        title__icontains=term,
        tags__icontains=term,
        description__icontains=term,
    )
    return render(request, 'user/category.html', {'category': term, 'wallpapers': wallpapers})


def test(request):
    return render(request, 'user/test.html')
