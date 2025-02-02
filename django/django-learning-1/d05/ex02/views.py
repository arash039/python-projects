import os
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from .forms import InputForm

# Create your views here.

LOG_FILE = settings.LOG_FILE_PATH

def ex02_view(request):
	form = InputForm()
	history = []

	if os.path.exists(LOG_FILE):
		with open(LOG_FILE, 'r') as file:
			history = file.readlines()

	if request.method == "POST":
		form = InputForm(request.POST)
		if form.is_valid():
			user_input = form.cleaned_data['text']
			timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			log_enrty = f"{timestamp} - {user_input}\n"

			with open(LOG_FILE, 'w') as file:
				file.write(log_enrty)
			
			history.append(log_enrty)
	return render(request, 'ex02/index.html', {'form': form, 'history': history})

