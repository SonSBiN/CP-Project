from django.shortcuts import render


def landing(request):
    return render(
        request,
        'main_page/main_page.html'
    )
