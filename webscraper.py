#Import Requests, BeautifulSoup 4 and Pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Takes a URL, stores the input as a variable called response. Becomes a bs4 object.
url = input("Please enter the address of the URL you would like to scrape: ")
response = requests.get(url)

#BeautifulSoup html parser
soup = BeautifulSoup(response.text, 'html.parser')

# create an empty list to store the links and titles
url_and_titles = []

# find all the links on the page and extract their URLs and titles
for link in soup.find_all("a"):
    href = link.get("href")
    title = link.get("title") or link.text.strip()
    url_and_titles.append({"URL": href, "title": title})

result = pd.DataFrame(url_and_titles)
result.to_csv("urls_and_titles.csv", index=False)
print(result)