import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_html_components.Img import Img




def create_layout():
   
    

    first_card = dbc.Card(

       [ 
        dbc.CardImg(src="/assets/paola.png", top=True),  
        dbc.CardBody(
            [
                html.H4("Paola Rojas Castañeda", className="card-title"),
                html.P( "MsC, computing science.",  className="card-text"),
                dbc.Button("✉ Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button(" LinkedIn",   href="", className="btnAbout"),

            ]
        )
       ],

       className="cardAbout"
    )


    second_card = dbc.Card(
        [  
        dbc.CardImg(src="/assets/manu.png", top=True),     
        dbc.CardBody(
             [
                html.H4("Manuela Escobar Sierra", className="card-title"),
                html.P("PhD. Engineering.",  className="card-text"),
                dbc.Button("📧 Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button("Linkedin",   href="", className="btnAbout"),
  ]
        )
       ],

       className="cardAbout"
    )

    third_card = dbc.Card(
        [  
        dbc.CardImg(src="/assets/alejo.png", top=True),
        dbc.CardBody(
             [
                html.H4("Alejandro Marin Marin", className="card-title"),
                html.P( "Ingeniero Mecatrónico.", className="card-text" ),
                dbc.Button("📧 Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button("Linkedin",   href="", className="btnAbout"),
 ]
        )
       ],
       className="cardAbout"
    )

    four_card = dbc.Card(
        [  
        dbc.CardImg(src="/assets/fabio.png", top=True),
        dbc.CardBody(
             [
                html.H4("Fabio Alejandro Hurtado", className="card-title"),
                html.P("Ingeniero de Sistemas", className="card-text" ),
                dbc.Button("📧 Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button("Linkedin",   href="https://www.linkedin.com/in/fabio-alejandro-hurtado-pe%C3%B1a-a2a97a210/", className="btnAbout"),
]
        )
       ],
       className="cardAbout"
    )

    five_card = dbc.Card(
        [  
        dbc.CardImg(src="/assets/ricardo.png", top=True),
        dbc.CardBody(
             [
                html.H4("Ricardo Ibarra Ibarra", className="card-title"),
                html.P("Ingeniero Mecánico", className="card-text" ),
                dbc.Button("📧 Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button("Linkedin",   href="", className="btnAbout"),

            ]
        )
       ],
       className="cardAbout"
    )

    six_card = dbc.Card(
        [  
        dbc.CardImg(src="/assets/alvaro.png", top=True),
        dbc.CardBody(
             [
                html.H4("Alvaro Jose Guijarro", className="card-title"),
                html.P("Ingeniero Industrial", className="card-text" ),
                dbc.Button("📧 Correo",   href="paola@gmail.com", className="btnAbout"),
                dbc.Button("Linkedin",   href="", className="btnAbout"),

            ]
        )
       ],
       className="cardAbout"
    )
    

    cards = dbc.Row(
        [
            dbc.Col(first_card, width=4),
            dbc.Col(second_card, width=4),
            dbc.Col(third_card, width=4),
            dbc.Col(four_card, width=4),
            dbc.Col(five_card, width=4),
            dbc.Col(six_card, width=4),
        ]
    )
    
    return dbc.Card([
            
            cards,
    ]) 
    
