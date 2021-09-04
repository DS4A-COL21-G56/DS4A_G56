import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_html_components.Div import Div
from dash_html_components.Img import Img

def create_layout():

    first_card = dbc.Card(
        [ 
            dbc.CardImg(src="/assets/img/paola.png", top=True, className="foto"),  
            html.Div(
                [
                    html.H4("Paola Rojas Castañeda", className=""),
                    html.P( "MsC, computing science.",  className=""),
                    dbc.Button("✉ Correo",   href="mailto:gpaolarojas@gmail.com", className="button mr-3 "),
                    dbc.Button(" LinkedIn",   href="https://www.linkedin.com/in/paola-rojas-castaneda/", className="button "),

                ]
            )
        ],
       className=" md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    second_card = dbc.Card(
        [  
            dbc.CardImg(src="/assets/img/manu.png", top=True, className="foto"),     
            html.Div(
                [
                    html.H4("Manuela Escobar Sierra", className=""),
                    html.P("PhD. Engineering.",  className=""),
                    dbc.Button("✉ Correo",   href="mailto:manuelaescobar@gmail.com", className="button mr-3 "),
                    dbc.Button("Linkedin",   href="https://co.linkedin.com/in/manuela-escobar-sierra-248152102", className="button "),
                ]
            )
       ],
       className="md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    third_card = dbc.Card(
        [  
            dbc.CardImg(src="/assets/img/alejo.png", top=True, className="foto"),
            html.Div(
                [
                    html.H4("Alejandro Marin Marin", className=""),
                    html.P( "Ingeniero Mecatrónico.", className="" ),
                    dbc.Button("✉ Correo",   href="alejomacar@hotmail.com", className="button mr-3 "),
                    dbc.Button("Linkedin",   href="https://www.linkedin.com/in/alejandro-marin-cardona/", className="button "),
                ]
            )
        ],
       className=" md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    four_card = dbc.Card(
        [  
            dbc.CardImg(src="/assets/img/fabio.png", top=True, className="foto"),
            html.Div(
                [
                    html.H4("Fabio Alejandro Peña", className=""),
                    html.P("Ingeniero de Sistemas.", className="" ),
                    dbc.Button("✉ Correo",   href="mailto:fabioamu824@gmail.com", className="button mr-3 "),
                    dbc.Button("Linkedin",   href="https://www.linkedin.com/in/fabio-alejandro-hurtado-pe%C3%B1a/", className="button "),
                ]
            )
       ],
       className="md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    five_card = dbc.Card(
        [  
            dbc.CardImg(src="/assets/img/ricardo.png", top=True, className="foto"),
            html.Div(
                [
                    html.H4("Ricardo Ibarra Ibarra", className=""),
                    html.P("Ingeniero Mecánico.", className="" ),
                    dbc.Button("✉ Correo",   href="mailto:raib1997@gmail.com", className="button mr-3 "),
                    dbc.Button("Linkedin",   href="https://www.linkedin.com/in/ricardoibarra97/", className="button "),

                ]
            )
       ],
       className="md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    six_card = dbc.Card(
        [  
            dbc.CardImg(src="/assets/img/alvaro.png", top=True, className="foto"),

            html.Div(
                [

                   
                        html.H4("Alvaro Jose Guijarro", className=""),
                        html.P("Ingeniero Industrial.", className="" ),      
                        dbc.Button("✉ Correo",   href="mailto:alvaroguijarro97@gmail.com", className="button mr-3"),
                        dbc.Button("Linkedin",   href="http://linkedin.com/in/alvaro-jose-guijarro-may-9b9056169", className="button"),
                                      

                ]
            )
        ],
       className="md-4 sm-12 mb-2 text-center mt-5",
       style={'padding':'2% 2% 10% 2%'}
    )

    cards = dbc.Row(
        [
            dbc.Col(first_card),
            dbc.Col(second_card),
            dbc.Col(third_card),            
                      
        ]
    )

    cards2 = dbc.Row(
        [
            dbc.Col(four_card),
            dbc.Col(five_card),
            dbc.Col(six_card),
        ]
    )

    
   
    
    return html.Div([  
            html.H1("ABOUT US", className="tittle"),          
            cards,
            cards2
    ]) 
    
