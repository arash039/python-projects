from .views import django_page, display_page, templates_page
from django.urls import path

urlpatterns = [
	path('django/', django_page, name='django'),
	path('display/', display_page, name='display'),
	path('templates/', templates_page, name='templates')
]
