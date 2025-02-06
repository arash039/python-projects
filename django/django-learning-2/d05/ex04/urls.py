from django.urls import path
from .views import populate, display, init, remove
urlpatterns = [
	path("init/", init, name="init"),
	path("populate/", populate, name="populate"),
	path("display/", display, name="display"),
	path("remove/", remove, name="remove"),
]