from django.shortcuts import render
from ex10.forms import CharacterFilterForm
from ex10.models import People, Movies, Planets

def character_search(request):
	results = []
	if request.method == 'POST':
		form = CharacterFilterForm(request.POST)
		if form.is_valid():
			min_date = form.cleaned_data['min_release_date']
			max_date = form.cleaned_data['max_release_date']
			planet_diameter = form.cleaned_data['planet_diameter']
			gender = form.cleaned_data['gender']

			characters = People.objects.filter(
				gender=gender,
				homeworld__diameter__gte=planet_diameter
			)

			movies = Movies.objects.filter(
				release_date__gte=min_date,
				release_date__lte=max_date
			)

			for movie in movies:
				for character in movie.characters.filter(id__in=characters):
					results.append({
						'character_name': character.name,
						'gender': character.gender,
						'film_title': movie.title,
						'homeworld_name': character.homeworld.name,
						'homeworld_diameter': character.homeworld.diameter,
					})

	else:
		form = CharacterFilterForm()

	return render(request, 'ex10/search.html', {
		'form': form,
		'results': results,
	})
#python manage.py loaddata ../resources/ex10_initial_data.json