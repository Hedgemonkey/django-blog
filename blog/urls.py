from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostLst.as_view(), name='home'),
]