#Ranking ATP

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_league_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tablelist=[]
    atp_table = soup.find('div', class_ = 'table-rankings')
    for team in atp_table.find_all('tbody'):
        rows = team.find_all('tr')
        for row in rows:
            pl_rank = row.find('td', class_='rank-cell').text.strip()
            pl_player = row.find('td', class_='player-cell').text.strip()
            pl_age = row.find('td', class_='age-cell').text.strip()
            pl_points = row.find('td', class_='points-cell').text.strip()
            teaminleague = {
                'puesto': pl_rank,
                'jugador': pl_player,
                'edad': pl_age,
                'puntos': pl_points
            }
            tablelist.append(teaminleague)
    return(tablelist)

data = get_league_table('https://www.atptour.com/es/rankings/singles')
        
df = pd.DataFrame(data)
df.to_csv('atp_ranking.csv')
df.to_excel('atp_ranking.xlsx')
print('archivo guardado')