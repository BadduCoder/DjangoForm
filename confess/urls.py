from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path('confess/new',views.confessnow, name="confess_new"),
]