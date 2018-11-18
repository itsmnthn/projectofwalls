"""wallpapermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from walls import views
urlpatterns = [
    path('', views.home, name="home"),

    path('test', views.test, name="test"),

    path('contact-us', views.contact_us, name="contact_us"),

    path('reset/password', views.reset_password, name="reset_password"),

    path('about/', views.about, name="about"),

    path('wallpaper', views.wallpaper, name="wallpaper"),

    path('wallpaper/<str:category>/<str:slug>',
         views.wallpaper, name="wallpaper"),

    path('profile/', views.profile, name="profile"),

    path('categories/', views.categories, name='Categories'),

    path('download/', views.download, name='download'),

    path('like/', views.like, name='like'),

    path('category/<str:cat_name>', views.category, name='category'),

    path('wallpaper/upload', views.wallpaper_upload, name='wallpaper_upload'),

    path('tag/<str:tag>', views.tag, name='tag'),
    path('search/', views.search, name='tag'),
]
