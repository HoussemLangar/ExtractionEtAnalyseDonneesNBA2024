import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page à scraper
url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

# Envoi de la requête HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Recherche de la table des statistiques
table = soup.find("table", {"id": "per_game_stats"})

# Extraction des données de la table
headers = [th.text for th in table.find("thead").find_all("th")]
data = []

for row in table.find("tbody").find_all("tr"):
    cells = [td.text for td in row.find_all("td")]
    if cells:  # Ignore les lignes vides
        data.append(cells)

# Création d'un DataFrame avec Pandas
df = pd.DataFrame(data, columns=headers[1:])  # Enlève la 1ère colonne vide

# Exporter le fichier CSV initial
df.to_csv("nba_stats_2024.csv", index=False)

# Abbreviations and their full names
team_names = {
     "PHI": "Philadelphia 76ers",
    "DAL": "Dallas Mavericks",
    "MIL": "Milwaukee Bucks",
    "OKC": "Oklahoma City Thunder",
    "NYK": "New York Knicks",
    "PHO": "Phoenix Suns",
    "BOS": "Boston Celtics",
    "SAC": "Sacramento Kings",
    "CLE": "Cleveland Cavaliers",
    "GSW": "Golden State Warriors",
    "DEN": "Denver Nuggets",
    "MIN": "Minnesota Timberwolves",
    "LAL": "Los Angeles Lakers",
    "ATL": "Atlanta Hawks",
    "MEM": "Memphis Grizzlies",
    "CHO": "Charlotte Hornets",
    "LAC": "Los Angeles Clippers",
    "UTA": "Utah Jazz",
    "NOP": "New Orleans Pelicans",
    "DET": "Detroit Pistons",
    "ORL": "Orlando Magic",
    "POR": "Portland Trail Blazers",
    "WAS": "Washington Wizards",
    "2TM": "2 Team",
    "IND": "Indiana Pacers",
    "SAS": "San Antonio Spurs",
    "HOU": "Houston Rockets",
    "MIA": "Miami Heat",
    "BRK": "Brooklyn Nets"
}

# Utilisation du dictionnaire pour ajouter les noms complets au DataFrame
df['Team Full'] = df['Team'].map(team_names)

# Ajouter les noms complets des postes
positions = {
    "PG": "Point Guard",
    "SG": "Shooting Guard",
    "SF": "Small Forward",
    "PF": "Power Forward",
    "C": "Center",
}

df['Pos Full'] = df['Pos'].map(positions)

# Exporter le fichier CSV nettoyé
df.to_csv("nba_stats_2024_cleaned.csv", index=False)

# Convertir la colonne 'PTS' en float
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')

# Exporter le fichier CSV des 10 meilleurs joueurs
top_players = df.nlargest(10, 'PTS')[['Player', 'Age', 'Awards']]
top_players.to_csv("top_10_best_players.csv", index=False)

