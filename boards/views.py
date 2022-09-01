from django.http import HttpResponse


def board_app_home(request):
    return HttpResponse("Board app")