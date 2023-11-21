import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://medes.ee/lood/'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Assuming blog titles are in <h2> tags, modify as per your site's structure


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for title in soup.find_all('h2'):
        print(title.text.strip())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
