from django.contrib import admin
from .models import Comment, Category, Article


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Article, ArticleAdmin)
