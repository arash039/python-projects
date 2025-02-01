import requests
from bs4 import BeautifulSoup
import sys
import re

def get_wikipedia_content(topic):
	formatted_topic = topic.replace(' ', '_')
	url = f"https://en.wikipedia.org/wiki/{formatted_topic}"
	
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except requests.RequestException as e:
		print(f"Error accessing Wikipedia: {e}")
		sys.exit(1)

def get_page_title(soup):
	title_element = soup.find(id="firstHeading")
	return title_element.text.strip() if title_element else None

def find_first_valid_link(soup):
	content = soup.find(id="mw-content-text")
	if not content:
		return None

	parser_output = content.find('div', class_='mw-parser-output')
	if not parser_output:
		return None

	for paragraph in parser_output.find_all('p', recursive=False):
		if not paragraph.text.strip() or paragraph.find('span', class_='mw-empty-elt'):
			continue

		for link in paragraph.find_all('a'):
			if (link.find_parent('table') or 
				link.find_parent('sup') or 
				link.find_parent('span', class_='reference')):
				continue

			if is_in_parentheses(link) or is_in_italics(link):
				continue

			href = link.get('href', '')
			
			if (href and 
				href.startswith('/wiki/') and 
				':' not in href and 
				not href.startswith('/wiki/File:') and
				not href.startswith('/wiki/Help:') and
				not href.startswith('/wiki/Wikipedia:') and
				'#' not in href):
				return href.split('/wiki/')[1]
	
	return None

def is_in_parentheses(link):
	current = link
	text_before = ""
	text_after = ""
	
	while current.previous_sibling:
		current = current.previous_sibling
		if hasattr(current, 'string') and current.string:
			text_before = str(current.string) + text_before

	current = link
	while current.next_sibling:
		current = current.next_sibling
		if hasattr(current, 'string') and current.string:
			text_after += str(current.string)

   
	open_count = text_before.count('(') - text_before.count(')')
	
	if open_count > 0:
		close_count = text_after.count(')')
		if close_count >= open_count:
			return True
	
	return False

def is_in_italics(link):
	return (link.find_parent('i') is not None or 
			link.find_parent('em') is not None)

def check_for_redirect(soup):
	redirect = soup.find('div', class_='redirectMsg')
	if redirect:
		link = redirect.find('a')
		if link:
			return link.get('href', '').split('/wiki/')[1]
	return None

def roads_to_philosophy():
	if len(sys.argv) != 2:
		print("Usage: python roads_to_philosophy.py <Wikipedia article>")
		sys.exit(1)

	start_topic = sys.argv[1]
	visited_pages = []
	current_topic = start_topic

	while True:
		html_content = get_wikipedia_content(current_topic)
		soup = BeautifulSoup(html_content, 'html.parser')
		
		redirect_target = check_for_redirect(soup)
		if redirect_target:
			current_topic = redirect_target
			continue
		
		page_title = get_page_title(soup)
		if not page_title:
			print("It leads to a dead end!")
			break
			
		visited_pages.append(page_title)
		print(page_title)
		
		if page_title == "Philosophy":
			print(f"{len(visited_pages)} roads from {start_topic} to philosophy")
			break
			
		next_topic = find_first_valid_link(soup)
		if not next_topic:
			print("It leads to a dead end!")
			break
			
		if next_topic in visited_pages:
			print("It leads to an infinite loop!")
			break
			
		current_topic = next_topic

if __name__ == "__main__":
	roads_to_philosophy()