from django.http import HttpResponse
from django.db import connection
import psycopg2
from django.db import transaction



def init(request):
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS ex08_planets (
					id SERIAL PRIMARY KEY,
					name VARCHAR(64) UNIQUE NOT NULL,
					climate VARCHAR(128),
					diameter INTEGER,
					orbital_period INTEGER,
					population BIGINT,
					rotation_period INTEGER,
					surface_water REAL,
					terrain VARCHAR(128)
				);
			"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS ex08_people (
					id SERIAL PRIMARY KEY,
					name VARCHAR(64) UNIQUE NOT NULL,
					birth_year VARCHAR(32),
					gender VARCHAR(32),
					eye_color VARCHAR(32),
					hair_color VARCHAR(32),
					height INTEGER,
					mass REAL,
					homeworld VARCHAR(64) REFERENCES ex08_planets(name)
				);
			"""
			)
		return HttpResponse("Tables created successfully.")
	except Exception as e:
		return HttpResponse(f"Error: {str(e)}")

def populate(request):
	try:
		with transaction.atomic():
			planets_csv_path = '../resources/planets.csv'
			try:
				with open(planets_csv_path, 'r') as f:
					with connection.cursor() as cursor:
						cursor.copy_from(f, 'ex08_planets', sep='\t', null='NULL',
										 columns=('name', 'climate', 'diameter', 'orbital_period', 
												  'population', 'rotation_period', 'surface_water', 'terrain'))
			except Exception as e:
				return HttpResponse(f"Error inserting planets: {str(e)}")

			people_csv_path = '../resources/people.csv'
			try:
				with open(people_csv_path, 'r') as f:
					with connection.cursor() as cursor:
						# Insert all data directly into ex08_people
						cursor.copy_from(f, 'ex08_people', sep='\t', null='NULL',
										 columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color',
												  'height', 'mass', 'homeworld'))

			except Exception as e:
				return HttpResponse(f"Error inserting people: {str(e)}")

		return HttpResponse("OK")

	except Exception as e:
		return HttpResponse(f"Error: {str(e)}")

def display(request):
	try:
		# Query to fetch character names, homeworld, and climate,
		# but only if homeworld exists in ex08_planets
		with connection.cursor() as cursor:
			cursor.execute("""
				SELECT p.name, pl.name AS homeworld, pl.climate
				FROM ex08_people p
				LEFT JOIN ex08_planets pl ON p.homeworld = pl.name
				WHERE pl.name IS NOT NULL
				AND (pl.climate ILIKE '%windy%')
				ORDER BY p.name;
			""")
			results = cursor.fetchall()

		if not results:
			return HttpResponse("<h2>No characters found with a windy homeworld.</h2>")

		response_html = """
		<html>
			<head><title>Characters Display</title></head>
			<body>
				<h2>Characters with 'Windy' or 'Moderately Windy' Climates</h2>
				<table border="1">
					<tr>
						<th>Character Name</th>
						<th>Homeworld</th>
						<th>Climate</th>
					</tr>
		"""
		for row in results:
			response_html += f"""
			<tr>
				<td>{row[0]}</td>
				<td>{row[1]}</td>
				<td>{row[2]}</td>
			</tr>
			"""
		response_html += """
				</table>
			</body>
		</html>
		"""

		return HttpResponse(response_html)

	except Exception as e:
		return HttpResponse(f"Error: {str(e)}")


# def populate_old(request):
# 	try:
# 		with transaction.atomic():  # Ensure all or nothing execution
# 			with connection.cursor() as cursor:
# 				planets_csv_path = '../resources/planets.csv'
# 				with open(planets_csv_path, 'r') as f:
# 					cursor.copy_from(f, 'ex08_planets', sep='\t', null='NULL',
# 									 columns=('name', 'climate', 'diameter', 'orbital_period', 
# 											  'population', 'rotation_period', 'surface_water', 'terrain'))

# 				cursor.execute("CREATE TEMP TABLE temp_people AS TABLE ex08_people WITH NO DATA;")

# 				people_csv_path = '../resources/people.csv'
# 				with open(people_csv_path, 'r') as f:
# 					cursor.copy_from(f, 'temp_people', sep='\t', null='NULL',
# 									 columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 
# 											  'height', 'mass', 'homeworld'))  # homeworld is stored as a NAME

# 				cursor.execute("""
# 					SELECT DISTINCT tp.homeworld 
# 					FROM temp_people tp
# 					LEFT JOIN ex08_planets p ON tp.homeworld = p.name
# 					WHERE p.name IS NULL AND tp.homeworld IS NOT NULL;
# 				""")

# 				missing_planets = cursor.fetchall()

# 				if missing_planets:
# 					missing_list = ", ".join([p[0] if p[0] is not None else "NULL" for p in missing_planets])
# 					return HttpResponse(f"Error: Missing planets in ex08_planets - {missing_list}")

# 				cursor.execute("""
# 					INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
# 					SELECT tp.name, tp.birth_year, tp.gender, tp.eye_color, tp.hair_color, tp.height, tp.mass, tp.homeworld
# 					FROM temp_people tp
# 					WHERE tp.homeworld IS NOT NULL
# 					AND tp.name NOT IN (SELECT name FROM ex08_people);
# 				""")


# 		return HttpResponse("Data inserted successfully.")

# 	except Exception as e:
# 		return HttpResponse(f"Error: {str(e)}")



# def display_old(request):
# 	try:
# 		with connection.cursor() as cursor:
# 			cursor.execute("""
# 				SELECT p.name, pl.name AS homeworld, pl.climate
# 				FROM ex08_people p
# 				JOIN ex08_planets pl ON p.homeworld = pl.name
# 				WHERE pl.climate ILIKE '%windy%'
# 				ORDER BY p.name;
# 			""")
# 			results = cursor.fetchall()

# 		response_html = """
# 		<html>
# 			<head><title>Characters Display</title></head>
# 			<body>
# 				<h2>Characters with "Windy" or "Moderately Windy" Climates</h2>
# 				<table border="1">
# 					<tr>
# 						<th>Character Name</th>
# 						<th>Homeworld</th>
# 						<th>Climate</th>
# 					</tr>
# 		"""
# 		for row in results:
# 			response_html += f"""
# 			<tr>
# 				<td>{row[0]}</td>
# 				<td>{row[1]}</td>
# 				<td>{row[2]}</td>
# 			</tr>
# 			"""
# 		response_html += """
# 				</table>
# 			</body>
# 		</html>
# 		"""
		
# 		return HttpResponse(response_html)
	
# 	except Exception as e:
# 		return HttpResponse(f"Error: {str(e)}")

