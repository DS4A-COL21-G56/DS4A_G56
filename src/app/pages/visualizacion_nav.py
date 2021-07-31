import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from app import app

"""
        * NO UTILIZADO

Implementacion alternativa de la pagina visualizacion utilizando vinculos
de navegacion ("NavLink") del paquete dash_bootstrap_components
"""

def create_layout():

    buttons = html.Div(
        [
            html.H2("Visualización", className="display-5"),
            dbc.Nav(
                [
                    dbc.NavLink("Notas", href="/page-2/notas", active="exact", className="buttons"),
                    dbc.NavLink("Género", href="/page-2/genero", active="exact", className="buttons"),
                    dbc.NavLink("Colegio", href="/page-2/colegio", active="exact", className="buttons"),
                    dbc.NavLink("Edad", href="/page-2/edad", active="exact", className="buttons"),
                ],
                vertical=False,
                # pills=True,
            ),
        ]
    )

    visualization = html.Div(
        id="visualization-content",
        className="content",
    )

    return html.Div(
        [
            dcc.Location(id="url-2"),
            buttons,
            visualization
        ])


@app.callback(Output("visualization-content", "children"), [Input("url-2", "pathname")])
def render_visualization(pathname):
    if pathname == "/page-2/notas":
        return html.P("Aca va la pagina")
    elif pathname == "/page-2/genero":
        return html.P("Aca va la pagina")
    elif pathname == "/page-2/colegio":
        return html.P("Aca va la pagina")
    elif pathname == "/page-2/edad":
        return html.P("Aca va la pagina")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )