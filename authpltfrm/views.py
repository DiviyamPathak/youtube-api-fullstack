from django.shortcuts import render


def home(request):
    # You can pass data to the template through the context dictionary
    context = {
        "title": "My Home Page",
        "message": "Welcome to my Django site!",
    }
    return render(request, "authpltfrm/auth.html", context)
