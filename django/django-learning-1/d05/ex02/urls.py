from django.urls import path
from .views import ex02_view
urlpatterns = [
	path('', ex02_view, name='ex02'),
]
