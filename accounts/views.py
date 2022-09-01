from django.http import HttpResponse


def accounts_app_home(request):
    return HttpResponse("Accounts app")