
#import libraries
import requests 
from bs4 import BeautifulSoup

# notify progress
print('Starting web scraper')

# define url
url = "https://www.learncodinganywhere.com/codingBootcamps/"
response = requests.get(url)

# define the soup object
soup = BeautifulSoup(response.text, 'html.parser')

title_element = soup.find('title')
if title_element:
    page_title = title_element.text
    print('Page Title:', page_title)
else:
    print('Page title not found')

footer_element = soup.find('footer')
if footer_element:
    page_footer = footer_element.text
    print('Footer:', page_footer)
else:
    print('No footer found')