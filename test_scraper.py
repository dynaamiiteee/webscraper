import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

print(soup.prettify())

# # Example: Extracting all links
# for link in soup.find_all('a'):
#     print(link.get('href'))
# # Example: Extracting all images
# for img in soup.find_all('img'):
#     print(img.get('src'))
# # Example: Extracting all headings
# for heading in soup.find_all(['h1', 'h2', 'h3']):
#     print(heading.text)
# # Example: Extracting all paragraphs
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)
# # Example: Extracting all lists
# for list_item in soup.find_all('li'):
#     print(list_item.text)
# # Example: Extracting all tables
# for table in soup.find_all('table'):
#     print(table.text)
# # Example: Extracting all divs
# for div in soup.find_all('div'):
#     print(div.text)
# # Example: Extracting all spans
# for span in soup.find_all('span'):
#     print(span.text)
# # Example: Extracting all forms
# for form in soup.find_all('form'):
#     print(form.text)
# # Example: Extracting all buttons
# for button in soup.find_all('button'):
#     print(button.text)
# # Example: Extracting all sections
# for section in soup.find_all('section'):
#     print(section.text)
# # Example: Extracting all articles
# for article in soup.find_all('article'):
#     print(article.text)
# # Example: Extracting all footers
# for footer in soup.find_all('footer'):
#     print(footer.text)

# # Example: Extracting data from a specific class
# for item in soup.find_all(class_='item-class'):
#     print(item.text)

# try:
#     # Your scraping logic here
#     print("Scraping completed successfully.")
# except AttributeError as e:
#     print(f"AttributeError: {e}")
# except requests.exceptions.RequestException as e:
#     print(f"RequestException: {e}")

# # Example: Storing data in a list
# data = []
# for item in soup.find_all(class_='data-item'):
#     data.append(item.text)

# print(data)
# # Example: Saving data to a file
# with open('output.txt', 'w') as f:
#     for item in data:
#         f.write(f"{item}\n")