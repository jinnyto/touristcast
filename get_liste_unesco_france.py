import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://fr.wikipedia.org/wiki/Liste_du_patrimoine_mondial_en_France"

try:
    page_response = requests.get(url, timeout=5)  
    data = []
    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content,'lxml')
        table1 = page_content.find('table', attrs={'class':'wikitable sortable'})
        table_body = table1.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [c.text.strip() for c in cols]
            data.append([x for x in cols if x]) 
        headers =['Site','Régions françaises','Type','Date','Sup(ha)','UNESCO','Notes','Coordonnées','Illus.']
        data.pop(0)
        df = pd.DataFrame(data, columns=headers)
        df.to_csv("Liste du patrimoine mondial en France.csv")
except requests.Timeout as e:
        print('Timeout occurred for requested page: ' + url)
        print(str(e))
