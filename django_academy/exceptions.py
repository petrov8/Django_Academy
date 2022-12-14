from django.shortcuts import render

def handle_400(request, exception):
    return render(request, "exceptions/403.html", status=400)

def handle_403(request, exception):
    return render(request, "exceptions/403.html", status=403)

def handle_404(request, exception):
    return render(request, "exceptions/404.html", status=404)

def handle_500(request):
    return render(request, "exceptions/500.html", status=500)


