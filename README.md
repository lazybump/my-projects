# Job Application Bots

Python scripts to automate job applications to save time

# Pre-requisites

You will need Python installed, and the Selenium package

# Explanation

2 scripts for 2 different online job boards: [Office Angels](https://www.office-angels.com/), and [Brook Street](https://www.brookstreet.co.uk/jobs/admin-and-secretarial/greater-london/)

(Made while looking for admin jobs a while back)

Each script runs from the first to the very last page, and applies to every single job in between that fits the criteria

You will need to adjust the personal details and preferred job stored in the variables to your own.

# Limitations

It can break due to asynchronisation i.e the script may continue executing commands before the page has fully loaded (however this is very unlikely to happen)

It may apply to the same job multiple times (in the event that the script breaks and you have to start it from the beginning) but this can be circumvented by starting the job/page counter from where you left off on the last execution



# Dota Web Scraper

Scrapes the Dota website to obtain the top Dota players and their rank at any given moment.

# Pre-requisites

You will need Selenium and Beautiful Soup, along with Requests

# Explanation

Comments to help understand each step

# Murdery Mystery

Fun little game implementing SQL to find the culprits of a murder. Comments included to explain the queries
