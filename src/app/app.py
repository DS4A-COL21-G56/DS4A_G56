import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('data/cleaned/perfil_ingreso_v2.csv')
data = df.groupby('COLEGIO_PROCEDENCIA').CODIGO.count().to_frame().sample(10).reset_index()

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "UBoyaca: attrition"

app.layout = html.Div(
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
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="highschool-barplot",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["COLEGIO_PROCEDENCIA"],
                                    "y": data["CODIGO"],
                                    "type": "bar",
                                    "hovertemplate": "%{y:d}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "High schools",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                #"height": 700,  # px
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    #"tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["COLEGIO_PROCEDENCIA"],
                                    "y": data["CODIGO"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "High schools, but a line",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)