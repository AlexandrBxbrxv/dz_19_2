from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'slug')
    list_filter = ('is_published',)
    search_fields = ('title',)
