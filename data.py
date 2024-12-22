import pandas as pd

def load_data():
    # Charger les données principales
    df = pd.read_csv('nba_stats_2024_cleaned.csv')

    # Charger les données des meilleurs joueurs
    df_top_players = pd.read_csv('top_10_best_players.csv')

    # Calculer les moyennes par équipe
    age_avg_by_team = df.groupby('Team Full')['Age'].mean().reset_index()
    pts_avg_by_team = df.groupby('Team Full')['PTS'].mean().reset_index()

    # Créer des options pour les listes déroulantes
    team_options = [{'label': team, 'value': team} for team in df['Team Full'].dropna().unique()]
    age_options = [{'label': int(age), 'value': int(age)} for age in sorted(df['Age'].dropna().unique())]

    return df, df_top_players, age_avg_by_team, pts_avg_by_team, team_options, age_options
