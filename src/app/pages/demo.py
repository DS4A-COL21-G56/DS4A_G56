import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Br
import pandas as pd
from dash.dependencies import Output, Input
from app import app

df = pd.read_csv('data/cleaned/perfil_ingreso_v2.csv')
# data = df.groupby('COLEGIO_PROCEDENCIA').CODIGO.count().to_frame().sample(10).reset_index()
data = df


def create_layout():

    return html.Div(
        children=[
            html.Div(
                children=[
                    html.P(children="👥👩🏽‍🎓👨🏽‍🎓", className="header-emoji"),
                    html.H1(

                        children="¡Bienvenido a Baco!", className="header-title"
                    ),
                    html.P(
                        children="Analyzing the behavior of student's attrition",
                       
                        className="header-description",
                    ),
                ],
                className="header",

            ),

            html.Div(
                
                    html.P(
                    " Being able to identify the factors that contribute to University student attrition"
                    " rates will greatly increase its capability of taking early action in their current struggle to help maintain"
                    " its student body in their institution and help them complete their bachelors and masters programs. We are hopeful"
                    " that by determining what variables contribute the most to a student’s decision to drop out of its selected program,"
                    " the Universty will create new retention strategies and strengthen its institutional programs that tackle"
                    " the desertion issue.",


                    className="body-description"

                ),
                className="body"
            ),

            html.Div([
                html.Label(" 📅 Periodo Actual\n 2020-2",className="info"),
                html.Label(" 👨‍🎓🎓👩‍🎓 Estudiantes Activos 5350",className="activos"),
                html.Label(" ⚠️ Alertas de deserción  33", className = "alertas")
             ]
            ),

            html.Div(
                html.Label("Facultades: ",  className="tituloFacultad"),

            ),

            html.Div([
                html.Label("👨‍💻 Ingenieria 2863", className="facultades"),
                html.Label("🏥 Medicina 684",  className="facultades"),
                html.Label("📚 Sociales 70",  className="facultades"),
                html.Label("🎨 Arte 207",  className="facultades")

            ]),
            
        ]
    )
