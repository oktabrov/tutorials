import requests
import json
url = 'https://openlibrary.org/search.json'
subject = input("Enter a subject: ")
param = {'q': subject,
         'limit': 10,
         'fields': "title,author_name,first_publish_year,number_of_pages_median"}
print("Fetching top 10 results...\n")
data = requests.get(url=url, params=param).json()
lst_of_books = data["docs"]
number_of_pages_median, first_publish_year = 0, float('inf')
name1, name2 = '', ''
for i in lst_of_books:
    if 'number_of_pages_median' in i and i['number_of_pages_median'] > number_of_pages_median:
        number_of_pages_median = i['number_of_pages_median']
        name1 = i['title']
    if 'first_publish_year' in i and i['first_publish_year'] < first_publish_year:
        first_publish_year = i['first_publish_year']
        name2 = i['title']
print("--- Analysis Results ---")
print("Thickest Book:")
print(f"Title: {name1}")
print(f"Pages: {number_of_pages_median}\n")
print("Oldest Book:")
print(f"Title: {name2}")
print(f"Pages: {first_publish_year}")