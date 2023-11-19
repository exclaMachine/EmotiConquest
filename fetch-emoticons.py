import requests
from bs4 import BeautifulSoup
import json

def fetch_emoticons():
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": "List_of_emoticons",
        "format": "json",
        "prop": "text"
    }

    response = requests.get(url, params=params)
    data = response.json()
    page_html = data["parse"]["text"]["*"]

    soup = BeautifulSoup(page_html, 'html.parser')
    emoticons = {}

    tables = soup.findAll('table', {'class': 'wikitable'})

    for table in tables:
        rows = table.findAll('tr')
        for row in rows:
            cells = row.findAll('td')
            if cells and len(cells) > 1:
                # Extracting all emoticons from icon cells
                icons = []
                for cell in cells[:-1]:  # All but the last cell
                    icons.extend([icon.strip() for icon in cell.get_text(separator='|').split('|')])

                # Extracting emojis from the last cell
                emojis = cells[-1].get_text().strip()

                # Mapping each emoticon to the emojis
                for icon in icons:
                    if icon:  # Ensuring the icon is not empty
                        emoticons[icon] = emojis

    return emoticons

if __name__ == "__main__":
    emoticons_data = fetch_emoticons()

    # Save the data to a file
    with open('emoticons_data.json', 'w', encoding='utf-8') as file:
        json.dump(emoticons_data, file, indent=4)
