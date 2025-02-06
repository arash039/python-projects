from django.shortcuts import render
from .models import People, Planets

def display(request):
    # Filter planets with windy or moderately windy climate
    windy_people = People.objects.filter(
        homeworld__climate__icontains='windy'
    ).order_by('name')
    
    if not windy_people.exists():
        context = {
            'no_data': True,
            'command': 'python manage.py loaddata ../resources/ex09_initial_data.json'
        }
    else:
        context = {
            'people': windy_people,
            'no_data': False
        }
    
    return render(request, 'ex09/display.html', context)