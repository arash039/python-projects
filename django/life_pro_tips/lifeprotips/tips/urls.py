from django.urls import path
from .views import home, register, user_login, user_logout, upvote_tip, downvote_tip, delete_tip, get_username

urlpatterns = [
	path('', home, name='home'),
	path('register/', register, name='register'),
	path('login/', user_login, name='login'),
	path('logout/', user_logout, name='logout'),
	path('upvote/<int:tip_id>/', upvote_tip, name='upvote_tip'),
	path('downvote/<int:tip_id>/', downvote_tip, name='downvote_tip'),
	path('delete/<int:tip_id>/', delete_tip, name='delete_tip'),
	path('get-username/', get_username, name='get_username'),
]
