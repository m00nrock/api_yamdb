from re import search
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from reviews.models import User, Category, Comment, Genre, Review, Title

#admin.site.register(User, UserAdmin)

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', )
    list_filter = ('name',)
    empty_value_display = '-пусто-'

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

@admin.register(Title)
class TitleAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'

#@admin.register(Comment, CommentAdmin)
#@admin.register(Category, CategoryAdmin)
#@admin.register(Genre, GenreAdmin)
#@admin.register(Title, TitleAdmin)
#@admin.register(Review, ReviewAdmin)
