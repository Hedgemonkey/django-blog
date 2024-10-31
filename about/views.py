from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import About
from .forms import CollaborateForm
from django.contrib import messages



# Create your views here.
def about(request):
    """
    Select the most recently updated object in :model:`about.About` and display it in the about page.
    """
    about = About.objects.order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if not about:
        raise Http404("No About object found.")
    
    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Collaboration request received! We'll get back to you soon.")
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )