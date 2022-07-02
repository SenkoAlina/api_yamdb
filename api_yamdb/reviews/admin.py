from django.contrib import admin
from .models import Review, Title, Comment, Category, Genre


class TitleAdmin(admin.ModelAdmin):

    list_display = ('id',)


class CommentAdmin(admin.ModelAdmin):

    list_display = ('review', 'text', 'author',)


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'author', 'score', 'title',)

    search_fields = ('text',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug',)

    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug',)

    search_fields = ('name',)


admin.site.register(Review, ReviewAdmin)

admin.site.register(Title, TitleAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Category, CategoryAdmin,)

admin.site.register(Genre, GenreAdmin)
