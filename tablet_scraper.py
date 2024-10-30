import requests
from bs4 import BeautifulSoup

def scrape_tablet_description(tablet_name):
    search_url = f"https://www.drugs.com/search.php?searchterm={tablet_name.replace(' ', '+')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Placeholder code: Adjust based on actual website structure
    description = soup.find('div', class_='tablet-description').text.strip()
    
    return description or "Description not found."