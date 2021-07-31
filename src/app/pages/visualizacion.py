import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash
from app import app
import pandas as pd


def create_layout():

    buttons = html.Div(
        [
            html.H2("Visualización", className="display-5"),
            html.Div([
                html.Button("Notas", id='btn-notas', n_clicks=0, className="buttons"),
                html.Button("Género", id='btn-genero', n_clicks=0, className="buttons"),
                html.Button("Colegio", id='btn-colegio', n_clicks=0, className="buttons"),
                html.Button("Edad", id='btn-edad', n_clicks=0, className="buttons"),
                ]
            )
        ]
    )

    visualization = html.Div(
        id="visualization-content",
        # className="content",
    )

    return html.Div(
        [
            buttons,
            visualization,
        ])

@app.callback(Output('visualization-content', 'children'),
              Input('btn-notas', 'n_clicks'),
              Input('btn-genero', 'n_clicks'),
              Input('btn-colegio', 'n_clicks'),
              Input('btn-edad', 'n_clicks'))
def displayClick(btn1, btn2, btn3, btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-notas' in changed_id:
        msg = "Actualizar la grafica para Notas aqui"
    elif 'btn-genero' in changed_id:
        msg = "Actualizar la grafica para Género aqui"
    elif 'btn-colegio' in changed_id:
        msg = "Actualizar la grafica para Colegio aqui"
    elif 'btn-edad' in changed_id:
        msg = "Actualizar la grafica para Edad aqui"
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)