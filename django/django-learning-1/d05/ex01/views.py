from django.shortcuts import render

# Create your views here.
def django_page(request):
	return render(request, 'ex01/page.html', {
		'title': 'Ex01: Django, framework web.',
		'content': """ Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.
        It was created in 2003 by Adrian Holovaty and Simon Willison and officially released in 2005.
        Django follows the "batteries-included" philosophy, offering built-in features like authentication, ORM, and admin interface. """,
		'stylesheet': 'style1.css'
	})

def display_page(request):
	return render(request, 'ex01/page.html', {
		'title': 'Ex01: Display process of a static page.',
        'content': """
        When a user requests a static page in Django:
        1. The browser sends a request to the server.
        2. Django routes the request through urls.py.
        3. The view function processes the request and calls the appropriate template.
        4. The template engine renders the HTML and returns it as a response.
        5. The browser displays the rendered page.
        """,
        'stylesheet': 'style1.css'
	})

def templates_page(request):
	return render(request, 'ex01/page.html', {
        'title': 'Ex01: Template engine.',
        'content': """
        Django's template engine allows dynamic content rendering. Features include:
        - **Blocks**: Define reusable sections.
        - **Loops (`for ... in`)**: Iterate over lists.
        - **If statements**: Conditional rendering.
        - **Context variables**: Pass data to templates.

        Example:
        ```django
        {% for item in items %}
            <p>{{ item }}</p>
        {% endfor %}
        ```
        """,
        'stylesheet': 'style2.css'
    })