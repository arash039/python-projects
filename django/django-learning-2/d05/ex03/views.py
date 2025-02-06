from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse

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
			results.append(f"Error!: {e}")
	
	return HttpResponse("<br>".join(results))

def display(request):
	try:
		movies = Movies.objects.all()
		if not movies.exists():
			return HttpResponse("no data available")
		html = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
		for row in movies:
			html += f"<tr><td>{row.episode_nb}</td><td>{row.title}</td><td>{row.director}</td><td>{row.producer}</td><td>{row.release_date}</td></tr>"
		return HttpResponse(html)
	except Exception as e:
		return HttpResponse(f"Error: {e}")
