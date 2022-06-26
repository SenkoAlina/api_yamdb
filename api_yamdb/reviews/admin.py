from django.contrib import admin

from.models import Review, Title, Comment


class TitleAdmin(admin.ModelAdmin):

    list_display = ('text', 'id')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('review', 'text', 'author')


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'author', 'score', 'title')

    search_fields = ('text',)


admin.site.register(Review, ReviewAdmin)

admin.site.register(Title, TitleAdmin)

admin.site.register(Comment, CommentAdmin)
