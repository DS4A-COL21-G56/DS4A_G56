import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Br
from dash_html_components.Div import Div
from dash_html_components.Img import Img
from dash_html_components.Link import Link
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Output, Input
from app import app

from pages import data, visualizacion

#df = pd.read_csv('data/cleaned/mat_cursadas_rend_academico_v2.csv')


def create_layout():

    first_div = html.Div(

        html.Img(src="/assets/header.png",
                 className="figura-1"),

        className="header",
    )

    second_div = html.Div([

        html.P("¡WELCOME TO BACO!", className="tittle"),

        html.P("Feel free to explore the main segments of Baco, in which you will be able to see some general information about the"
               "University and its students, the attrition prediction model and its different modules, visualize the most significant data from"
               "the students dataset and check the relationships between them, as well as to meet the team that made it all posible.",

               className="pHome",
               ),
    ])

    first_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/prediction.png", top=True, className="imagen"),
            dbc.CardBody(
                [
                    html.H4("Attrition Prediction",
                            className="card-title"),
                    html.P("Check the attrition probabilityin every student’s case",
                           className="card-text"),
                    dcc.Link(html.Button('view detail', className="btnCard2"),
                             href="/prediction"),
                ]
            )
        ],
        className="bodyCard",
    )

    two_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/data.png", top=True, className="imagen"),
            dbc.CardBody(
                [
                    html.H4("Data",
                            className="card-title"),
                    html.P("See some general information regarding the population of students",
                           className="card-text"),
                    dcc.Link(html.Button('view detail', className="btnCard2"),
                             href="/data"),
                ]
            )
        ],
        className="bodyCard",
    )

    third_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/visualization.png", top=True, className="imagen"),
            dbc.CardBody(
                [
                    html.H4("Visualization",
                            className="card-title"),
                    html.P("Discover the diferent relationships and trends the dataset has to offer",
                           className="card-text"),
                    dcc.Link(html.Button('view detail', className="btnCard2"),
                             href="/visualization"),
                ]
            )
        ],

        className="bodyCard",
    )

    four_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/about.png", top=True, className="imagen"),
            dbc.CardBody(
                [
                    html.H4("About Us",
                            className="card-title"),
                    html.P("Get to know the team that created Baco",
                           className="card-text"),
                    dcc.Link(html.Button('view detail', className="btnCard4"),
                             href="/aboutUs"),
                ]
            )
           
        ],

         className="bodyCard",
    )

    cards = dbc.Row([

        dbc.Col(first_card, width=3),
        dbc.Col(two_card, width=3),
        dbc.Col(third_card, width=3),
        dbc.Col(four_card, width=3),
    ]
    )

    return html.Div([
        first_div,
        second_div,
        cards,

    ])
