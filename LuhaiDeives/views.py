from django.shortcuts import render, loader


def index(request):

    context = {

        'template':'Hello World'
    }
    return render(request, template_name='index.html', context=context)