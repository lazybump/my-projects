# Import relevant libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# File path for the webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# List of Dota player regions
all_regions = ['americas', 'europe', 'se_asia', 'china']

# Function will use the provided argument to construct a URL and go that webpage
def scrape(region):
    # Go to Dota Leaderboards page
    driver.get(f'https://www.dota2.com/leaderboards/#{region}-0')
    # Give the page a second to load everything
    time.sleep(1)
    # Grab the page source and put it into a variable
    webpage = driver.page_source
    # Parse the page source as a soup object
    soup = BeautifulSoup(webpage, 'html.parser')
    # Find the table tag
    table = soup.tbody
    # Find all rows in table and put them into a list
    rows = table.find_all('tr')
    # Initialize lists to capture data
    rankings = []
    players = []
    country_codes = []
    # Append each row's rank, and player name into rankings, and players respectively
    for row in rows:
        rank_tag = row.td
        rankings.append(rank_tag.string)
        player_tag = rank_tag.next_sibling
        players.append(player_tag.get_text().strip())
        # Try to find & append the player's country code to the country codes list
        try:
            flag = row.img['src']
            country_code = flag[-6:-4]
            country_codes.append(country_code)
        # Some players have no country listed, so replace missing values with 'N/A' and append to the list
        except:
            country_codes.append('N/A')
    # Put all 3 lists into a dictionary
    mydict = {'Division Rank': rankings, 'Player': players, 'Country': country_codes}
    # Put the dictionary into a dataframe
    df = pd.DataFrame(mydict)
    # Save the dataframe to a CSV file, after capitalising the region name. Also, remove default indexing
    df.to_csv(f'Dota leaderboards {region.title()}.csv', index=False)


# Now call the function over each element in the list of regions
for region in all_regions:
    scrape(region)