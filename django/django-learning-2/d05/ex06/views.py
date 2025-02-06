from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .forms import UpdateForm
from django.shortcuts import redirect
#from django import forms

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
			CREATE TABLE IF NOT EXISTS ex06_movies (
			title VARCHAR(64) UNIQUE NOT NULL,
			episode_nb SERIAL PRIMARY KEY,
			opening_crawl TEXT,
			director VARCHAR(32) NOT NULL,
			producer VARCHAR(128) NOT NULL,
			release_date DATE NOT NULL,
			created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
			updated TIMESTAMP WITH TIME ZONE DEFAULT NOW()
			);
		"""
		cursor.execute(create_table_query)

		create_trigger_function_query = """
			CREATE OR REPLACE FUNCTION update_changetimestamp_column()
			RETURNS TRIGGER AS $$
			BEGIN
				NEW.updated = now();
				NEW.created = OLD.created;
				RETURN NEW;
			END;
			$$ language 'plpgsql';
		"""

		cursor.execute(create_trigger_function_query)
		
		create_trigger_query = """
			CREATE TRIGGER update_films_changetimestamp
			BEFORE UPDATE ON ex06_movies
			FOR EACH ROW
			EXECUTE PROCEDURE update_changetimestamp_column();
		"""
		cursor.execute(create_trigger_query)
	
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
				INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
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
		cursor.execute("SELECT * FROM ex06_movies")
		rows = cursor.fetchall()

		cursor.close()
		conn.close()

		if not rows:
			return HttpResponse("No data available")
		html = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Opening Crawl</th><th>Created</th><th>Updated</th></tr>"
		for row in rows:
			html += f"<tr><td>{row[1]}</td><td>{row[0]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[2]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>"
		html += "</table>"

		return HttpResponse(html)

	except Exception as e:
		return HttpResponse(f"Error: {str(e)}", status=500)
	
def updates(request):
	if request.method == "POST":
		form = UpdateForm(request.POST)
		if form.is_valid():
			episode_nb = form.cleaned_data['episode_nb']
			opening_crawl = form.cleaned_data['opening_crawl']
			print(f"opening: {opening_crawl}")
			try:
				conn = psycopg2.connect(
					dbname="djangotraining",
					user="djangouser",
					password="secret",
					host="localhost",
					port="5432"
				)
				cursor = conn.cursor()
				update_query = """
					UPDATE ex06_movies
					SET opening_crawl = %s
					WHERE episode_nb = %s;
				"""
				cursor.execute(update_query, (opening_crawl, episode_nb))
				conn.commit()
				cursor.close()
				conn.close()
				return redirect("update")
			except Exception as e:
				return HttpResponse(f"Error: {str(e)}", status=500)
		else:
			print(form.errors)
	else:
		form = UpdateForm()

	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()

		cursor.execute("SELECT episode_nb, title FROM ex06_movies;")
		movies = cursor.fetchall()

		cursor.close()
		conn.close()
		csrf_token = get_token(request)
		movie_options = ""
		for movie in movies:
			movie_options += f'<option value="{movie[0]}">{movie[1]}</option>'
		if movies:
			html_form = f"""
				<!DOCTYPE html>
				<html>
				<head>
					<title>Update Movie</title>
				</head>
				<body>
					<h1>Update Movie Opening Crawl</h1>
					<form method="post">
						<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
						<label for="id_episode_nb">Movie:</label>
						<select name="episode_nb" id="id_episode_nb">
							{movie_options}
						</select><br><br>
						<label for="id_opening_crawl">Opening Crawl:</label><br>
						<textarea name="opening_crawl" id="id_opening_crawl" rows="10" cols="50"></textarea><br><br>
						<button type="submit">Update</button>
					</form>
				</body>
				</html>
			"""
			return HttpResponse(html_form)
		else:
			return HttpResponse("No data available!")
	except Exception as e:
		return HttpResponse(f"No data available {str(e)}")
	
def update(request):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT episode_nb, title FROM ex06_movies;")
		movies = cursor.fetchall()
		cursor.close()
		conn.close()
	except Exception as e:
		return HttpResponse(f"No data available {str(e)}")

	movie_choices = [(str(movie[0]), movie[1]) for movie in movies]
	print(movie_choices)
	if request.method == "POST":
		print("POST Data:", request.POST)
		form = UpdateForm(request.POST, movies=movie_choices)
		
		if form.is_valid():
			episode_nb = form.cleaned_data['episode_nb']
			opening_crawl = form.cleaned_data['opening_crawl']
			print(f"Form is valid! Updating {episode_nb} with text: {opening_crawl}")

			try:
				conn = psycopg2.connect(
					dbname="djangotraining",
					user="djangouser",
					password="secret",
					host="localhost",
					port="5432"
				)
				cursor = conn.cursor()
				update_query = """
					UPDATE ex06_movies
					SET opening_crawl = %s
					WHERE episode_nb = %s;
				"""
				cursor.execute(update_query, (opening_crawl, episode_nb))
				conn.commit()
				cursor.close()
				conn.close()
				return redirect("update")
			except Exception as e:
				return HttpResponse(f"Error: {str(e)}", status=500)
		else:
			print("Form errors:", form.errors)

	else:
		form = UpdateForm()

	csrf_token = get_token(request)
	movie_options = "".join(
		f'<option value="{movie[0]}">{movie[1]}</option>' for movie in movies
	)

	html_form = f"""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Update Movie</title>
		</head>
		<body>
			<h1>Update Movie Opening Crawl</h1>
			<form method="post">
				<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
				<label for="id_episode_nb">Movie:</label>
				<select name="episode_nb" id="id_episode_nb">
					{movie_options}
				</select><br><br>
				<label for="id_opening_crawl">Opening Crawl:</label><br>
				<textarea name="opening_crawl" id="id_opening_crawl" rows="10" cols="50"></textarea><br><br>
				<button type="submit">Update</button>
			</form>
		</body>
		</html>
	"""
	return HttpResponse(html_form)
