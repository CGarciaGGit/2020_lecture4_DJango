from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("<str:name>", views.greet, name="greet"),
	path("carlo", views.carlo, name="Carlo"),
	path("david", views.david, name="david")
]