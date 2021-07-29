import dash_core_components as dcc
import dash_html_components as html
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
                        children=[
                            html.Div(children="Column", className="menu-title"),
                            dcc.Dropdown(
                                id="column-filter",
                                options=[
                                    {"label": col, "value": col}
                                    for col in ['GENERO', 'EDAD', 'COLEGIO_PROCEDENCIA']
                                ],
                                value="GENERO",
                                clearable=False,
                                className="dropdown",
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.Div(children="Sample", className="menu-title"),
                            dcc.Dropdown(
                                id="sample-filter",
                                options=[
                                    {"label": str(n_sample), "value": n_sample}
                                    for n_sample in range(1,31)
                                ],
                                value=5,
                                clearable=False,
                                searchable=False,
                                className="dropdown",
                            ),
                        ],
                    ),
                    # html.Div(
                        # children=[
                            # html.Div(
                                # children="Date Range",
                                # className="menu-title"
                                # ),
                            # dcc.DatePickerRange(
                                # id="date-range",
                                # min_date_allowed=data.Date.min().date(),
                                # max_date_allowed=data.Date.max().date(),
                                # start_date=data.Date.min().date(),
                                # end_date=data.Date.max().date(),
                            # ),
                        # ]
                    # ),
                ],
                className="menu",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id="highschool-barplot", config={"displayModeBar": False},
                        ),
                        className="card",
                    ),
                    html.Div(
                        children=dcc.Graph(
                            id="highschool-lineplot", config={"displayModeBar": False},
                        ),
                        className="card",
                    ),
                ],
                className="wrapper",
            ),
        ]
    )


@app.callback(
    [Output("highschool-barplot", "figure"), Output("highschool-lineplot", "figure")],
    [
        Input("column-filter", "value"),
        Input("sample-filter", "value"),
        # Input("date-range", "start_date"),
        # Input("date-range", "end_date"),
    ],
)
def update_charts(col, n_sample):#, start_date, end_date):
    # mask = (
        # (data.col == col)
        # & (data.type == sample)
        # & (data.Date >= start_date)
        # & (data.Date <= end_date)
    # )
    # filtered_data = data.loc[mask, :]
    if col == 'GENERO':
        filtered_data = data.groupby(col).CODIGO.count().to_frame().reset_index()
    else:
        filtered_data = data.groupby(col).CODIGO.count().to_frame().sample(n_sample).reset_index()

    barplot_figure = {
        "data": [
            {
                "x": filtered_data[col],
                "y": filtered_data["CODIGO"],
                "type": "bar",
                "hovertemplate": "%{y:d}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "High schools",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    lineplot_figure = {
        "data": [
            {
                "x": filtered_data[col],
                "y": filtered_data["CODIGO"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "High schools, but a line", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return barplot_figure, lineplot_figure