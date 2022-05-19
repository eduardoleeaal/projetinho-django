from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Eduardo Leal'
    })
    # return HTTP response


def contato(request):
    return HttpResponse('CONTATO')
    # return HTTP response


def sobre(request):
    return HttpResponse('SOBRE')
    # return HTTP response
