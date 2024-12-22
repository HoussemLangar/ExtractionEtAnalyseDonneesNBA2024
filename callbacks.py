from dash import Input, Output
import plotly.express as px
from data import load_data

df, *_ = load_data()

def register_callbacks(app):
    # Callback
    @app.callback(
        [
            #Output
            Output('player-points-graph', 'figure'),
            Output('player-matches-graph', 'figure'),
            Output('player-starters-graph', 'figure'),
            Output('player-shooting-graph', 'figure'),
            Output('player-ftm-graph', 'figure'),
            Output('player-stl-graph', 'figure'),
            Output('player-tov-graph', 'figure'),
            Output('player-pf-graph', 'figure'),
            Output('player-mp-graph', 'figure')
        ],
        [
            #Input
            Input('team-dropdown', 'value'),
            Input('team-dropdown-matches', 'value'),
            Input('team-dropdown-starters', 'value'),
            Input('team-dropdown-shooting', 'value'),
            Input('team-dropdown-ftm', 'value'),
            Input('team-dropdown-stl', 'value'),
            Input('team-dropdown-tov', 'value'),
            Input('team-dropdown-pf', 'value'),
            Input('team-dropdown-mp', 'value')
        ]
    )

    #Mettre à jour les graphiques
    def update_graphs(selected_team, selected_team_matches, selected_team_starters, selected_team_shooting, selected_team_ftm, selected_team_stl, selected_team_tov, selected_team_pf, selected_team_mp):
        
        # Filtrer les données en fonction de l'équipe sélectionnée
        filtered_df = df[df['Team Full'] == selected_team]
        filtered_df_matches = df[df['Team Full'] == selected_team_matches]
        filtered_df_starters = df[df['Team Full'] == selected_team_starters]
        filtered_df_shooting = df[df['Team Full'] == selected_team_shooting]
        filtered_df_ftm = df[df['Team Full'] == selected_team_ftm]
        filtered_df_stl = df[df['Team Full'] == selected_team_stl]
        filtered_df_tov = df[df['Team Full'] == selected_team_tov]
        filtered_df_pf = df[df['Team Full'] == selected_team_pf]
        filtered_df_mp = df[df['Team Full'] == selected_team_mp]

        # Graphique: Points par joueur
        fig_player_points = px.bar(
            filtered_df,
            x='Player', 
            y='PTS', 
            title=f'Points par Match par Joueur pour l\'équipe {selected_team}',
            labels={'Player': 'Joueur', 'PTS': 'Points par Match'}
        )

        # Graphique: Nombre de matches
        fig_player_matches = px.bar(
            filtered_df_matches,
            x='Player',
            y='MP',
            title=f'Nombre de Matches par Joueur pour l\'équipe {selected_team_matches}',
            labels={'Player': 'Joueur', 'MP': 'Nombre de Matches'}
        )

        # Graphique: Titulaires par joueur
        fig_player_starters = px.bar(
            filtered_df_starters,
            x='Player',
            y='GS',
            title=f'Titulaire par Joueur pour l\'équipe {selected_team_starters}',
            labels={'Player': 'Joueur', 'GS': 'Nombre de Titulaires'}
        )

        # Graphique: Pourcentage de réussite aux tirs par joueur
        fig_player_shooting = px.bar(
            filtered_df_shooting,
            x='Player',
            y='FG%',
            title=f'Pourcentage de Réussite aux Tirs par Joueur pour l\'équipe {selected_team_shooting}',
            labels={'Player': 'Joueur', 'FG%': 'Pourcentage de Réussite aux Tirs'}
        )

        # Graphique: Nombre moyen de lancers francs réussis par match
        fig_player_ftm = px.bar(
            filtered_df_ftm,
            x='Player',
            y='FT',
            title=f'Nombre Moyen de Lancers Francs Réussis par Match par Joueur pour l\'équipe {selected_team_ftm}',
            labels={'Player': 'Joueur', 'FT': 'Nombre Moyen de Lancers Francs Réussis'}
        )

        # Graphique: STL par joueur
        fig_player_stl = px.bar(
            filtered_df_stl,
            x='Player',
            y='STL',
            title=f'Interceptions Moyennes par Match (STL) pour l\'équipe {selected_team_stl}',
            labels={'Player': 'Joueur', 'STL': 'Interceptions Moyennes'}
        )

        # Graphique: TOV par joueur
        fig_player_tov = px.bar(
            filtered_df_tov,
            x='Player',
            y='TOV',
            title=f'Ballons Perdus Moyens par Match (TOV) pour l\'équipe {selected_team_tov}',
            labels={'Player': 'Joueur', 'TOV': 'Ballons Perdus Moyens'}
        )

        # Graphique: Fautes personnelles moyennes par match
        fig_player_pf = px.bar(
            filtered_df_pf,
            x='Player',
            y='PF',
            title=f'Fautes Personnelles Moyennes par Match pour l\'équipe {selected_team_pf}',
            labels={'Player': 'Joueur', 'PF': 'Fautes Personnelles Moyennes'}
        )

        # Graphique: Minutes moyennes par match
        fig_player_mp = px.bar(
            filtered_df_mp,
            x='Player',
            y='MP',
            title=f'Minutes Moyennes par Match pour l\'équipe {selected_team_mp}',
            labels={'Player': 'Joueur', 'MP': 'Minutes Moyennes'}
        )

        return fig_player_points, fig_player_matches, fig_player_starters, fig_player_shooting, fig_player_ftm, fig_player_stl, fig_player_tov, fig_player_pf, fig_player_mp
