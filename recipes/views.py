from django.shortcuts import HttpResponse  # , render


def home(request):
    return HttpResponse('HOME 1')
    # return HTTP response


def contato(request):
    return HttpResponse('CONTATO')
    # return HTTP response


def sobre(request):
    return HttpResponse('SOBRE')
    # return HTTP response
