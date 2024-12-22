from dash import Dash
from layout import create_layout
from callbacks import register_callbacks

# Initialiser l'application Dash
app = Dash(
    __name__,
    external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css']
)

# Configurer la mise en page
app.layout = create_layout(app)

# Enregistrer les callbacks
register_callbacks(app)

# Lancer l'application
if __name__ == '__main__':
    app.run_server(debug=True)
