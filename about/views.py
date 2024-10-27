from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About



# Create your views here.
def about(request):
    """
    Select the most recently updated object in :model:`about.About` and display it in the about page.
    """
    about = About.objects.order_by('-updated_on').first()
    if not about:
        raise Http404("No About object found.")
    return render(request, "about/about.html", {"about": about},)