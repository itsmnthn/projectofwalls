from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Categories, Feedback, TeamMembers, Wallpapers


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'modified_at', 'active', ]
    list_filter = ('active',)


@admin.register(Wallpapers)
class WallpapersAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploader', 'likes',
                    'downloads', 'views', 'created_at', 'modified_at', 'active', ]
    list_filter = ('category', 'uploader', 'active', 'location',)
    exclude = ('slug', 'likes', 'views',)
    summernote_fields = ('description',)
    search_fields = ['title', 'category__title', 'description',
                     'uploader__username', 'tags', 'location', ]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description',
                    'created_at', 'modified_at', 'active', ]
    list_filter = ('active',)


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone',
                    'created_at', 'modified_at', 'active', ]
    list_filter = ('active',)
