from django.shortcuts import render


from account.models import Account

def get(request):
    authors = Account.article.all()
    if authors:
        for author in authors:
            print("hello world")
