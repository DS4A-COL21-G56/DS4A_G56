from dash_bootstrap_components._components.Button import Button
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Br
from dash_html_components.Div import Div
from dash_html_components.Img import Img
from dash_html_components.Link import Link
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Output, Input
from src.app import app


#df = pd.read_csv('data/cleaned/mat_cursadas_rend_academico_v2.csv')


def create_layout():

    first_div = html.Div(
        children = [
            html.Img(src="/assets/img/header.png", className="figura-1"),
        ],
        className="header",
    )

    second_div = html.Div([

        html.P("WELCOME TO BACO", className="tittle"),

        html.P("Feel free to explore the main segments of Baco, in which you will be able to see some general information about the"
               "University and its students, the attrition prediction model and its different modules, visualize the most significant data from"
               "the students dataset and check the relationships between them, as well as to meet the team that made it all posible.",

               className="pHome",
               ),
    ])

    first_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/img/prediction.png", top=True, className="imagen"),
            html.Div(
                [
                    html.H4("Attrition Prediction",
                            className="title2"),
                    html.P("Estimate attrition probability for different student’s cases.",
                           className=""),
                   dcc.Link(dbc.Button('view detail', className=" button"), href="/prediction"),

                   
                ]
            )
        ],
        className="bodyCard  md-3 sm-12 mb-2 text-center mt-5",
    )

    two_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/img/data.png", top=True, className="imagen"),
            html.Div(
                [
                    html.H4("Data",
                            className="title2"),
                    html.P("See some general information regarding the population of students.",
                           className=""),
                    dcc.Link(dbc.Button('view detail', className=" button"), href="/data"),
                ]
            )
        ],
        className="bodyCard  md-3 sm-12 mb-2 text-center mt-5",
    )

    third_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/img/visualization.png", top=True, className="imagen"),
            html.Div(
                [
                    html.H4("Visualization",
                            className="title2"),
                    html.P("Discover the diferent relationships and trends the dataset has to offer.",
                           className=""),
                    dcc.Link(dbc.Button('view detail', className=" button"), href="/visualization"),
                ]
            )
        ],

        className="bodyCard  md-3 sm-12 mb-2 text-center mt-5",
    )

    four_card = dbc.Card(
        [

            dbc.CardImg(src="/assets/img/about.png", top=True, className="imagen"),
            html.Div(
                [
                    html.H4("About Us",
                            className="title2"),
                    html.P("Let's know abou the team which created Baco.",
                           className=""),
                    dcc.Link(dbc.Button('view detail', className=" button"), href="/aboutUs"),
                    
                ]
            )
           
        ],

         className="bodyCard  md-3 sm-12 mb-2 text-center mt-5 ",
    )

    cards = dbc.Row([

        dbc.Col(first_card),
        dbc.Col(two_card),
        dbc.Col(third_card),
        dbc.Col(four_card),
    ]
    )

    return html.Div([
        first_div,
        second_div,
        cards,

    ])
