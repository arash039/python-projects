from django import forms

# class UpdateForm(forms.Form):
# 	episode_nb = forms.ChoiceField(choices=[], label="Movie")
# 	opening_crawl = forms.CharField(widget=forms.Textarea, label="Opening Crawl")

# 	def __init__(self, *args, **kwargs):
# 		movies = kwargs.pop("movies", [])
# 		print(movies)
# 		super(UpdateForm, self).__init__(*args, **kwargs)
# 		self.fields['episode_nb'].choices = [(str(movie[0]), movie[1]) for movie in movies]
# 		print("Available Choices in Form:", self.fields['episode_nb'].choices)

class UpdateForm(forms.Form):
	episode_nb = forms.ChoiceField(choices=[], label="Movie")
	opening_crawl = forms.CharField(widget=forms.Textarea, label="Opening Crawl")

	def __init__(self, *args, **kwargs):
		movies = kwargs.pop("movies", [])
		super(UpdateForm, self).__init__(*args, **kwargs)

		self.fields['episode_nb'].choices = [(str(movie[0]), movie[1]) for movie in movies]

			
		