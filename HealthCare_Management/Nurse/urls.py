from django.urls import path
from . import views

urlpatterns = [

    path("", views.addDetails, name="Nurse_Details"),
    path("viewDetails/", views.viewDetails, name="viewDetails"),


]