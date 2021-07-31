import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash
from app import app
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned/perfil_ingreso_v2.csv')
cols = ["COLEGIO_PROCEDENCIA","ES_DESERTOR", "CODIGO", "EDAD","GENERO"]
data = df[df.COLEGIO_PROCEDENCIA != 'universidad'][cols]

data2 = pd.read_csv('data/cleaned/rendimiento_academico.csv')["NOTA_DEF"]


def create_layout():

    buttons = html.Div(
        [
            html.H2("Visualization", className="display-5"),
            html.Div([
                html.Button("Grades", id='btn-grades', n_clicks=0, className="buttons"),
                html.Button("Gender", id='btn-gender', n_clicks=0, className="buttons"),
                html.Button("High school", id='btn-school', n_clicks=0, className="buttons"),
                html.Button("Age", id='btn-age', n_clicks=0, className="buttons"),
                ]
            )
        ]
    )

    visualization = html.Div(
        children=dcc.Graph(
            id="visualization-content", config={"displayModeBar": False},
        ),
    )


    return html.Div(
        [
            buttons,
            visualization,
        ])

@app.callback(Output('visualization-content', 'figure'),
              Input('btn-grades', 'n_clicks'),
              Input('btn-gender', 'n_clicks'),
              Input('btn-school', 'n_clicks'),
              Input('btn-age', 'n_clicks'))
def displayClick(btn1, btn2, btn3, btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-grades' in changed_id:
        Data = data2
        x="NOTA_DEF"
        color=None
        title='Final Grade'
    elif 'btn-gender' in changed_id:
        Data = data
        x="GENERO"
        color= "GENERO"
        title='Students Gender'
    elif 'btn-school' in changed_id:
        Data = data
        x="COLEGIO_PROCEDENCIA"
        color="ES_DESERTOR"
        title='Origin High School'
    elif 'btn-age' in changed_id:
        Data = data
        x="EDAD"
        color="ES_DESERTOR"
        title='Student Attrition by age'
    else:
        Data = data
        x="EDAD"
        color="ES_DESERTOR"
        title='Student Attrition by age'

    return px.histogram(Data, x=x, color=color, color_discrete_sequence=["#DA7879", "#912F33"], title=title)