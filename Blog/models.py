from django.db import models

from account.models import Account
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=59, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='标题')
    author = models.ForeignKey(Account, on_delete=models.DO_NOTHING, verbose_name='作者', related_name='articles')
    context = models.CharField(max_length=5000, verbose_name='正文')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')

    # comments = models.ManyToManyRel(Comment, to=Comment, related_name='评论', related_query_name='所有评论')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    comment = models.CharField(max_length=400, verbose_name='评论内容')
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, related_name='comments')
    author = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
