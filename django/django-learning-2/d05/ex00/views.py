from django.shortcuts import render
import psycopg2
from django.http import HttpResponse

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
		cursor = conn.cursor() #cursor acts as a bridge between python code and database
		create_table_query = """
			CREATE TABLE IF NOT EXISTS ex00_movies (
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
	

