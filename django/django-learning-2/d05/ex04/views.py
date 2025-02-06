from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from django.middleware.csrf import get_token


# Create your views here.
def init(request):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		create_table_query = """
			CREATE TABLE IF NOT EXISTS ex04_movies (
			title VARCHAR(64) UNIQUE NOT NULL,
			episode_nb SERIAL PRIMARY KEY,
			opening_crawl TEXT,
			director VARCHAR(32) NOT NULL,
			producer VARCHAR(128) NOT NULL,
			release_date DATE NOT NULL
			);
		"""
		cursor.execute(create_table_query)
		conn.commit()

		cursor.close()
		conn.close()

		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"Error: {str(e)}", status=500)
	
def populate(request):
	movies_data = [
		{
			"episode_nb": 1,
			"title": "The Phantom Menace",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "1999-05-19"
		},
		{
			"episode_nb": 2,
			"title": "Attack of the Clones",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2002-05-16"
		},
		{
			"episode_nb": 3,
			"title": "Revenge of the Sith",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2005-05-19"
		},
		{
			"episode_nb": 4,
			"title": "A New Hope",
			"director": "George Lucas",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1977-05-25"
		},
		{
			"episode_nb": 5,
			"title": "The Empire Strikes Back",
			"director": "Irvin Kershner",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1980-05-17"
		},
		{
			"episode_nb": 6,
			"title": "Return of the Jedi",
			"director": "Richard Marquand",
			"producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
			"release_date": "1983-05-25"
		},
		{
			"episode_nb": 7,
			"title": "The Force Awakens",
			"director": "J. J. Abrams",
			"producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			"release_date": "2015-12-11"
		}
	]

	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()

		response = ""
		for movie in movies_data:
			try:
				inser_query = """
				INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
				VALUES (%s, %s, %s, %s, %s);
				"""
				cursor.execute(inser_query, (
					movie["episode_nb"],
					movie["title"],
					movie["director"],
					movie["producer"],
					movie["release_date"]
				))
				conn.commit()
				response += f"OK: {movie['title']}<br>"
			except Exception as e:
				conn.rollback()
				response += f"Error inserting {movie['title']}: {str(e)}<br>"
		cursor.close()
		conn.close()

		return HttpResponse(response)
	except Exception as e:
		return HttpResponse(f"Error: {str(e)}", status=500)
	
def display(request):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM ex04_movies")
		rows = cursor.fetchall()

		cursor.close()
		conn.close()

		if not rows:
			return HttpResponse("No data available")
		html = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
		for row in rows:
			html += f"<tr><td>{row[1]}</td><td>{row[0]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
		html += "</table>"

		return HttpResponse(html)

	except Exception as e:
		return HttpResponse(f"Error: {str(e)}", status=500)
	
def remove(request):
	try:
		csrf_token = get_token(request)
		
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT episode_nb, title FROM ex04_movies;") 
		movies = cursor.fetchall()

		if not movies:
			return HttpResponse("No data available")

		if request.method == "POST":
			print(request.POST.get("movie"))
			movie_id = request.POST.get("movie")
			if movie_id:
				cursor.execute("DELETE FROM ex04_movies WHERE episode_nb = %s;", [movie_id])
				conn.commit()
		
		cursor.execute("SELECT episode_nb, title FROM ex04_movies;")
		movies = cursor.fetchall()

		if not movies:
			return HttpResponse("No data available")

		html = f"""
		<form method="post">
			<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}" />
			<label for="movie">Select a movie to remove:</label>
			<select name="movie" id="movie">
		"""
		for movie in movies:
			html += f'<option value="{movie[0]}">{movie[1]}</option>'
		
		html += """
			</select>
			<button type="submit" name="remove">Remove</button>
		</form>
		"""

		return HttpResponse(html)

	except Exception as e:
		return HttpResponse(f"Error: {e}")

def remove_full(request):
	try:
		csrf_token = get_token(request)

		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()

		cursor.execute("SELECT episode_nb, title FROM ex04_movies;")
		movies = cursor.fetchall()

		if not movies:
			return HttpResponse("No data available")

		if request.method == "POST":
			movie_id = request.POST.get("movie")
			if movie_id:
				cursor.execute("DELETE FROM ex04_movies WHERE episode_nb = %s;", [movie_id])
				conn.commit()

			cursor.execute("SELECT episode_nb, title FROM ex04_movies;")
			movies = cursor.fetchall()

			if not movies:
				return HttpResponse("No data available")

		html = f"""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Remove Movie</title>
		</head>
		<body>
			<form method="post">
				<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}" />
				<label for="movie">Select a movie to remove:</label>
				<select name="movie" id="movie">
		"""

		for movie in movies:
			html += f'<option value="{movie[0]}">{movie[1]}</option>'

		html += """
				</select>
				<button type="submit" name="remove">Remove</button>
			</form>
		</body>
		</html>
		"""

		return HttpResponse(html)

	except Exception as e:
		return HttpResponse(f"Error: {e}")