from dash import dcc, html, dash_table
import plotly.express as px
from data import load_data

df, df_top_players, age_avg_by_team, pts_avg_by_team, team_options, age_options = load_data()

def create_layout(app):
    return html.Div([
        html.Div([
            html.H1("Statistiques NBA 2024", className='text-center mb-5 display-4 fw-bold text-primary py-4'),

            # Barre de navigation
            html.Div([
                html.Div([
                    html.A(name, href=f"#{id}", className='btn btn-outline-primary m-1')
                    for name, id in [
                        ("Âge Moyen par Équipe", "avg-age-by-team"),
                        ("Points Moyens par Équipe", "avg-pts-by-team"),
                        ("Meilleurs Joueurs", "top-10-players"),
                        ("Points des Joueurs par Équipe", "player-points-graph"),
                        ("Filtrer par Équipe et Âge", "player-table"),
                        ("Nombre de Matchs par Joueur", "player-matches-graph"),
                        ("Titulaires par Joueur", "player-starters-graph"),
                        ("Réussite aux Tirs", "player-shooting-graph"),
                        ("Lancers Francs", "player-ftm-graph"),
                        ("Interceptions", "player-stl-graph"),
                        ("Ballons Perdus", "player-tov-graph"),
                        ("Minutes Moyennes", "player-mp-graph"),
                        ("Fautes Personnelles", "player-pf-graph"),
                    ]
                ], className='text-center mb-4')
            ]),

        # Section principale contenant tous les graphiques
        # Ligne 1 : Graphiques "Âge Moyen par Équipe" et "Points Moyens par Équipe"
        html.Div([
            html.Div([
                html.H2("Âge Moyen par Équipe", className='text-center mb-3'),
                dcc.Graph(
                    id='avg-age-by-team',
                    figure=px.bar(age_avg_by_team, x='Team Full', y='Age',
                                  title='Âge Moyen par Équipe dans la NBA en 2024',
                                  labels={'Team Full': 'Équipe', 'Age': 'Âge Moyen'}).update_layout(template="plotly_dark"),
                    style={'marginTop': '20px'} 
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3'), 

            html.Div([
                html.H2("Points Moyens par Match par Équipe", className='text-center mb-3'),
                dcc.Graph(
                    id='avg-pts-by-team',
                    figure=px.bar(pts_avg_by_team, x='Team Full', y='PTS',
                                  title='Points Moyens par Match par Équipe dans la NBA en 2024',
                                  labels={'Team Full': 'Équipe', 'PTS': 'Points Moyens par Match'}),
                    style={'marginTop': '20px', 'margin-left': '10px'}
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3') 
        ], className='row'),

        # Ligne 2 : Meilleurs joueurs et Points des joueurs par équipe
        html.Div([
            # Meilleurs Joueurs de la NBA
            html.Div([
                html.H2("Meilleurs Joueurs de la NBA en 2024", className='text-center mb-3 text-danger fw-bold'),
                dcc.Graph(
                    id='top-10-players',
                    figure=px.bar(
                        df_top_players,
                        x='Player',
                        y='Awards',
                        title='Meilleurs Joueurs de la NBA par Récompenses en 2024',
                        labels={'Player': 'Joueur', 'Awards': 'Nombre de Récompenses'},
                        color='Awards', 
                    ).update_layout(
                        title_font=dict(size=20, color='gold', family='Arial Black'),
                        plot_bgcolor='rgba(0,0,0,0)',  
                        paper_bgcolor='rgba(0,0,0,0)', 
                        xaxis=dict(title='Joueurs', showgrid=False),
                        yaxis=dict(title='Récompenses', showgrid=True, gridcolor='gray')
                    ),
                    style={'marginTop': '20px'}
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-dark text-white p-3'),

            # Points des Joueurs par Équipe
            html.Div([
                html.H2("Points des Joueurs par Équipe", className='text-center mb-3 text-primary fw-bold'),
                dcc.Dropdown(
                    id='team-dropdown',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-points-graph',
                    style={
                        'marginTop': '20px',
                        'border': '2px solid #007bff',
                        'borderRadius': '10px',
                        'backgroundColor': '#f8f9fa'  
                    }
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-light p-3')
        ], className='row'),


        # Ligne 3 : Filtrer les joueurs par équipe et âge
        html.Div([
            html.Div([
                html.H2("Filtrer les Joueurs par Équipe et Âge", className='text-center mb-3'),

                # Liste déroulante pour l'équipe
                html.Label("Sélectionner une Équipe :", className='form-label'),
                dcc.Dropdown(
                    id='team-dropdown-filter',
                    options=team_options,
                    value=team_options[0]['value'],
                    clearable=False,
                    className='form-select mb-3'
                ),

                # Liste déroulante pour l'âge
                html.Label("Sélectionner un Âge :", className='form-label'),
                dcc.Dropdown(
                    id='age-dropdown-filter',
                    options=age_options,
                    value=age_options[0]['value'],
                    clearable=False,
                    className='form-select mb-3'
                ),

                # Tableau
                dash_table.DataTable(
                    id='player-table',
                    columns=[
                        {'name': 'Player', 'id': 'Player'},
                        {'name': 'Age', 'id': 'Age'},
                        {'name': 'Team Full', 'id': 'Team Full'},
                        {'name': 'PTS', 'id': 'PTS'}
                    ],
                    style_table={
                        'overflowX': 'auto', 
                        'marginLeft': 'auto', 
                        'marginRight': 'auto', 
                        'marginTop': '20px',
                        'width': '100%',  
                        'border': '1px solid #ccc',  
                        'backgroundColor': '#ffffff'  
                    },
                    style_cell={'textAlign': 'left', 'padding': '10px'},
                    style_header={'backgroundColor': '#007bff', 'fontWeight': 'bold', 'color': 'white'}
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3')  
        ], className='row'),

        # Ligne 4 : Nombre de Matchs par Joueur et Nombre de Matchs Comme Titulaire par Joueur
        html.Div([
            # Nombre de Matchs par Joueur par Équipe
            html.Div([
                html.H2("Nombre de Matchs par Joueur par Équipe", className='text-center mb-3 text-success fw-bold'),
                dcc.Dropdown(
                    id='team-dropdown-matches',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-matches-graph',
                    figure=px.bar(
                        df,  
                        x='Player',
                        y='G',
                        color='Team Full',
                        title="Nombre de Matchs par Joueur",
                        labels={'Player': 'Joueur', 'Matches': 'Matchs', 'Team Full': 'Équipe'},
                        template='seaborn' 
                    ).update_layout(
                        title_font=dict(size=20, color='#28a745', family='Verdana'),
                        plot_bgcolor='#f8f9fa',  
                        paper_bgcolor='#ffffff',  
                        xaxis=dict(title='Joueurs', showgrid=True, gridcolor='#e9ecef'),
                        yaxis=dict(title='Nombre de Matchs', showgrid=True, gridcolor='#e9ecef'),
                        legend=dict(title="Équipes", orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
                    ),
                    style={
                        'marginTop': '20px',
                        'border': '2px solid #28a745',
                        'borderRadius': '10px',
                        'backgroundColor': '#ffffff'
                    }
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-light p-3'),

            # Nombre de Matchs Comme Titulaire par Joueur par Équipe
            html.Div([
                html.H2("Nombre de Matchs Comme Titulaire par Joueur par Équipe", className='text-center mb-3 text-info fw-bold'),
                dcc.Dropdown(
                    id='team-dropdown-starters',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-starters-graph',
                    figure=px.scatter(
                        df, 
                        x='Player',
                        y='GS',
                        size='GS', 
                        color='Team Full',
                        title="Nombre de Matchs Comme Titulaire par Joueur",
                        labels={'Player': 'Joueur', 'Starters': 'Titulaires', 'Team Full': 'Équipe'},
                        template='plotly_white' 
                    ).update_layout(
                        title_font=dict(size=20, color='#17a2b8', family='Verdana'),
                        plot_bgcolor='#ffffff',  
                        paper_bgcolor='#ffffff', 
                        xaxis=dict(title='Joueurs', showgrid=True, gridcolor='#e9ecef'),
                        yaxis=dict(title='Titulaires', showgrid=True, gridcolor='#e9ecef'),
                        legend=dict(title="Équipes", orientation="v", yanchor="top", y=1, xanchor="right", x=1)
                    ),
                    style={
                        'marginTop': '20px',
                        'border': '2px solid #17a2b8',
                        'borderRadius': '10px',
                        'backgroundColor': '#ffffff'
                    }
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-light p-3')
        ], className='row'),

        
        # Ligne 5 : Pourcentage de Réussite aux Tirs par Joueur et Nombre Moyen de Lancers Francs Réussis par Match par Joueur
        html.Div([
            html.Div([
                html.H2("Pourcentage de Réussite aux Tirs par Joueur par Équipe", className='text-center mb-3'),
                dcc.Dropdown(
                    id='team-dropdown-shooting',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-shooting-graph',
                    style={'marginTop': '20px'}
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3'),

            html.Div([
                html.H2("Nombre Moyen de Lancers Francs Réussis par Match par Joueur par Équipe", className='text-center mb-3'),
                dcc.Dropdown(
                    id='team-dropdown-ftm',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-ftm-graph',
                    style={'marginTop': '20px'}
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3')
        ], className='row'),

        # Ligne 6 : Interceptions Moyennes par Match et Ballons Perdus Moyens par Match
        html.Div([
            html.Div([
                html.H2("Interceptions Moyennes par Match", className='text-center mb-3'),
                dcc.Dropdown(
                    id='team-dropdown-stl',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(id='player-stl-graph')
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3'),

            html.Div([
                html.H2("Ballons Perdus Moyens par Match", className='text-center mb-3'),
                dcc.Dropdown(
                    id='team-dropdown-tov',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(id='player-tov-graph')
            ], className='col-md-6 mb-4 mx-auto border rounded bg-white p-3')
        ], className='row'),

        # Ligne 7 : Minutes Moyennes par Match par Joueur et Fautes Personnelles Moyennes par Match
        html.Div([
            # Graphique 1 : Minutes Moyennes par Match (Diagramme à Bulles)
            html.Div([
                html.H2("Minutes Moyennes par Match par Joueur", className='text-center mb-3 text-primary fw-bold'),
                dcc.Dropdown(
                    id='team-dropdown-mp',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-mp-graph',
                    figure=px.scatter(
                        df, 
                        x='Player',
                        y='MP',
                        size='MP',  
                        color='Team Full',
                        title="Minutes Moyennes par Match (Diagramme à Bulles)",
                        labels={
                            'Player': 'Joueur',
                            'Minutes per Match': 'Minutes Moyennes',
                            'Team Full': 'Équipe',
                            'Games Played': 'Matchs Joués'
                        },
                        template='plotly',
                        hover_data=['MP']  
                    ).update_layout(
                        title_font=dict(size=22, color='#007bff', family='Verdana'),
                        plot_bgcolor='#f9f9f9',
                        paper_bgcolor='#ffffff',
                        xaxis=dict(title='Joueurs', showgrid=True, gridcolor='#e9ecef'),
                        yaxis=dict(title='Minutes Moyennes', showgrid=True, gridcolor='#e9ecef'),
                        legend=dict(title="Équipes", orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
                    ),
                    style={
                        'marginTop': '20px',
                        'border': '2px solid #007bff',
                        'borderRadius': '10px',
                        'backgroundColor': '#ffffff'
                    }
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-light p-3'),

            # Graphique 2 : Fautes Personnelles Moyennes (Graphique en Radar)
            html.Div([
                html.H2("Fautes Personnelles Moyennes par Match", className='text-center mb-3 text-danger fw-bold'),
                dcc.Dropdown(
                    id='team-dropdown-pf',
                    options=team_options,
                    value=df['Team Full'].dropna().iloc[0],
                    clearable=False,
                    className='form-select mb-3'
                ),
                dcc.Graph(
                    id='player-pf-graph',
                    figure=px.line_polar(
                        df, 
                        r='PF',  
                        theta='Player', 
                        color='Team Full',
                        line_close=True, 
                        title="Fautes Personnelles Moyennes par Match (Graphique Radar)",
                        labels={
                            'Player': 'Joueur',
                            'Personal Fouls per Match': 'Fautes Moyennes',
                            'Team Full': 'Équipe'
                        },
                        template='seaborn'
                    ).update_layout(
                        title_font=dict(size=22, color='#dc3545', family='Verdana'),
                        polar=dict(
                            bgcolor='#f8f9fa',
                            radialaxis=dict(showgrid=True, gridcolor='#e9ecef', tick0='Fautes Moyennes'),
                            angularaxis=dict(showgrid=True, gridcolor='#e9ecef', tick0='Joueurs')
                        ),
                        legend=dict(title="Équipes", orientation="v", yanchor="top", y=1, xanchor="right", x=1)
                    ),
                    style={
                        'marginTop': '20px',
                        'border': '2px solid #dc3545',
                        'borderRadius': '10px',
                        'backgroundColor': '#ffffff'
                    }
                )
            ], className='col-md-6 mb-4 mx-auto border rounded bg-light p-3'),
        ], className='row'),


        # Pied de page
        html.Footer("© 2024 NBA Dashboard. Tous droits réservés.", className='text-center')
        ])
    ])
