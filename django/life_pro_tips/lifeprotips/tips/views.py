from django.shortcuts import render, redirect, get_object_or_404
from .models import Tip
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, TipForm
from django.http import JsonResponse
from django.conf import settings
import random
from django.db.models import Count


# Create your views here.

CustomUser = get_user_model()

def home(request):
	#tips = Tip.objects.all().order_by('-date')
	tips = Tip.objects.annotate(upvote_count = Count('upvotedby')).order_by('-upvote_count')
	if request.method == 'POST' and request.user.is_authenticated:
		form = TipForm(request.POST)
		if form.is_valid():
			tip = form.save(commit=False)
			tip.author = CustomUser.objects.get(id=request.user.id)
			tip.save()
			return redirect('home')
	else:
		form = TipForm() if request.user.is_authenticated else None

	return render(request, 'tips/home.html', {'tips': tips, 'form': form})

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'tips/register.html', {'form' : form})

def user_login(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				return redirect('home')
	else:
		form = LoginForm()

	return render(request, 'tips/login.html', {'form' : form})

def user_logout(request):
	logout(request)
	return redirect('home')

@login_required
def downvote_tip(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)

	if request.user == tip.author or request.user.can_downvote():
		if request.user in tip.downvotedby.all():
			tip.downvotedby.remove(request.user)
		else:
			tip.downvotedby.add(request.user)
			tip.upvotedby.remove(request.user)

		tip.author.update_reputation()
	
	return redirect("home")

@login_required
def upvote_tip(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)

	if request.user in tip.upvotedby.all():
		tip.upvotedby.remove(request.user)
	else:
		tip.upvotedby.add(request.user)
		tip.downvotedby.remove(request.user)
	
	tip.author.update_reputation()
	return redirect("home")

@login_required
def delete_tip(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)

	if request.user == tip.author or request.user.can_delete_tips():
		tip.delete()

	return redirect("home")

def get_username(request):
	if request.user.is_authenticated:
		return JsonResponse({"username" : request.user.username})
	return JsonResponse({"username" : random.choice(settings.RANDOM_NAMES)})
