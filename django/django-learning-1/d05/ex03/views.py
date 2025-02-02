from django.shortcuts import render

# Create your views here.
def ex03_view(request):
    base_colors = {
        'noir': (0, 0, 0),
        'rouge': (255, 0, 0),
        'bleu': (0, 0, 255),
        'vert': (0, 255, 0),
    }

    rows = []
    for i in range(51):
        row = {}
        for color_name, base_color in base_colors.items():
            shade = tuple(max(0, min(255, int(c * (1 - i * 0.02)))) for c in base_color)
            row[color_name] = f'rgb({shade[0]}, {shade[1]}, {shade[2]})'
        rows.append(row)

    return render(request, 'ex03/index.html', {'rows': rows})

# def ex03_view(request):
# 	base_colors = {
# 		'noir': (0, 0, 0),
# 		'rouge': (255, 0, 0),
# 		'bleu': (0, 0, 255),
# 		'vert': (0, 255, 0),
# 	}

# 	def generate_shades(base_color):
# 		shades = []
# 		for i in range(51):
# 			shade = tuple(max(0, min(255, int(c * (1 - i * 0.02)))) for c in base_color)
# 			shades.append(f'rgb({shade[0]}, {shade[1]}, {shade[2]})')
# 		return shades
	
# 	color_shades = {
# 		'noir': generate_shades(base_colors['noir']),
# 		'rouge': generate_shades(base_colors['rouge']),
# 		'bleu': generate_shades(base_colors['bleu']),
# 		'vert': generate_shades(base_colors['vert']),
# 	}
# 	return render(request, 'ex03/index.html', {'color_shades': color_shades, 'range': range(51)})

