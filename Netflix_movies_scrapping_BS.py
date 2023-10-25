# 100 BEST MOVIES ON NETFLIX RANKED BY TOMATOMETER 

#importing necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

# Start measuring the execution time
start_time = time.time()

# URL of the webpage to scrape
url = 'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/?fbclid=IwAR0BOUz-htWPJZVuHUzImAXxxRD3vfaJjSieIf4Thm8p2xx9C1Ldz-UgGJA'

page = requests.get(url) # Sending a GET request to the URL and retrieving the webpage content
soup = BeautifulSoup(page.text, 'lxml') # Parsing the HTML content using BeautifulSoup and the lxml parser

# Scraping the movie links from the webpage
tags = soup.find_all('a',class_ = 'article_movie_poster') # Finding all <a> tags to get links
links = [tag['href'] for tag in tags] # Extracting the 'href' attribute from each <a> tag
#print(links)


df_links_info = pd.DataFrame({'Links': [''],'Title': [''], 'Rating_%': [''], 'Year': ['']}) # Creating an empty DataFrame for movies info

# Scrape and store the movie information for each link
for link in links: # Looping through each movie link
    html = requests.get(link) # Sending a GET request to the movie link and retrieving the webpage content
    html_soup = BeautifulSoup(html.text, 'lxml')
    title = html_soup.find('h1', class_ = 'title').text # Extracting the movie title from the HTML
    rating = html_soup.find('score-board').get('tomatometerscore') # Extracting the movie rating from the HTML
    year = html_soup.find('p', class_ = 'info').text[:4] # Extracting the movie release year from the HTML

    
    df_links_info = df_links_info.append({'Links': link,'Title': title, 'Rating_%': rating, 'Year': year},ignore_index=True) # Appending all information to the 'df_info_links' DataFrame

df_links_info.to_csv('C:/Users/rahil/Desktop/DSBA Master/warsaw university sPRING/Webscraping/Final Project/Netflixmovies.csv',index=False)
   
# Stop measuring the execution time
end_time = time.time()

# Calculate the running time
running_time = end_time - start_time
print("Running time: ", running_time, "seconds")
    