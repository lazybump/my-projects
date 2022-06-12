from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Go to Dota Leaderboards page
driver.get('https://www.dota2.com/leaderboards/#europe-0')

# Give the page a second to load everything
time.sleep(1)

# Grab the page source and put it into a variable
webpage = driver.page_source

# Parse the page source as a soup object
soup = BeautifulSoup(webpage, 'html.parser')

# Find all the rows and put them into a list
rows = soup.find_all('tr')

# For each row, get the text in 'td' tag which is the player's rank, and put that in a list called 'positions'
positions = []
for row in rows:
    rank = row.td.string
    positions.append(rank)

# For each row, get the text in the second 'td' tag which is the player's name, and put that in a list called 'players'
players = []
for row in rows:
    name = row.td.next_sibling.get_text().strip()
    players.append(name)

# Put both lists into a dictionary
mydict = {'Division Rank': positions, 'Player': players}

# Put the dictionary into a dataframe
df = pd.DataFrame(mydict)

# Save the dataframe to a CSV file
df.to_csv('Dota Leaderboards Scraped.csv', index=False)

# Voila