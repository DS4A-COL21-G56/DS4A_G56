import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from app import app

df = pd.read_csv('data/cleaned/mat_cursadas_rend_academico_v2.csv')
data = df.groupby('TOT_MAT_INSCRITAS')[['MAT_APROBADAS']].sum().reset_index()
# data = df


def create_layout():

    return html.Div(
        children=[
            html.Div(
                children=[
                    html.P(children="👥👩🏽‍🎓👨🏽‍🎓", className="header-emoji"),
                    html.H1(
                        children="Students' attrition - Universidad de Boyaca", className="header-title"
                    ),
                    html.P(
                        children="Analyzing the behavior of student's attrition"
                        " in the university of boyaca",
                        className="header-description",
                    ),
                ],
                className="header",
            ),
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": data["TOT_MAT_INSCRITAS"],
                            "y": data["MAT_APROBADAS"],
                            "type": "lines",
                        },
                    ],
                    "layout": {"title": "TOTAL_SUBJECT VS APPROVED_SUBJECT"},
                },
            ),
        ]
    )
