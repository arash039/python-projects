from django.urls import path
from .views import populate, display, init, update
urlpatterns = [
	path("init/", init, name="init"),
	path("populate/", populate, name="populate"),
	path("display/", display, name="display"),
	path("update/", update, name="update"),
]