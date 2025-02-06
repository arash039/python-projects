from django.shortcuts import render, redirect
from .models import Movies
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .forms import UpdateForm

# Create your views here.

def populate(request):
	data = [
		{
			'episode_nb': 1,
			'title': 'The Phantom Menace',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '1999-05-19'
		},
		{
			'episode_nb': 2,
			'title': 'Attack of the Clones',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '2002-05-16'
		},
		{
			'episode_nb': 3,
			'title': 'Revenge of the Sith',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '2005-05-19'
		},
		{
			'episode_nb': 4,
			'title': 'A New Hope',
			'director': 'George Lucas',
			'producer': 'Gary Kurtz, Rick McCallum',
			'release_date': '1977-05-25'
		},
		{
			'episode_nb': 5,
			'title': 'The Empire Strikes Back',
			'director': 'Irvin Kershner',
			'producer': 'Gary Kurtz, Rick McCallum',
			'release_date': '1980-05-17'
		},
		{
			'episode_nb': 6,
			'title': 'Return of the Jedi',
			'director': 'Richard Marquand',
			'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
			'release_date': '1983-05-25'
		},
		{
			'episode_nb': 7,
			'title': 'The Force Awakens',
			'director': 'J. J. Abrams',
			'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
			'release_date': '2015-12-11'
		}
	]

	results = []
	for item in data:
		try:
			Movies.objects.create(
				title = item["title"],
				episode_nb = item["episode_nb"],
				director = item["director"],
				producer = item["producer"],
				release_date = item["release_date"]
			)
			results.append("OK")
		except Exception as e:
			results.append(f"Error: {e}")
	return HttpResponse("<br>".join(results))

def display(request):
	try:
		movies = Movies.objects.all()
		if not movies.exists():
			return HttpResponse("no data available")
		html = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Opening Crawl</th><th>Created</th><th>Updated</th></tr>"
		for movie in movies:
			html += f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td><td>{movie.opening_crawl}</td><td>{movie.created}</td><td>{movie.updated}</td></tr>"
		return HttpResponse(html)
	except Exception as e:
		return HttpResponse(f"Error: {e}")
	
def update(request):
	if not Movies.objects.exists():
		return HttpResponse("No data available")
	if request.method == "POST":
		form = UpdateForm(request.POST)
		if form.is_valid():
			movie = form.cleaned_data['movie']
			movie.opening_crawl = form.cleaned_data['opening_crawl']
			movie.save()
			return HttpResponse("Update successful")
		return HttpResponse("Invalid form submission")
	csrf_token = get_token(request)
	 # as_p wrapps into <p>
	form_html = f"""
		<form method='post'>
		<input type='hidden' name='csrfmiddlewaretoken' value='{csrf_token}'>
		{UpdateForm().as_p()}
		<button type='submit'>Update</button>
		</form>
	"""
	return HttpResponse(form_html)