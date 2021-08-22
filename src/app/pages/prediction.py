import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import dash
import dash_table
from app import app
import pandas as pd
import plotly.express as px
from models import predictor

n, df = predictor.predict(2016, 2, 0.7)

table_params = dict()
table_params['year'] = None
table_params['period'] = None
table_params['treshold'] = None

dropdown_style =    {
                        "color": "black",
                        "background-color": "#ffffff",
                        "border-radius": "40px",
                        "box-shadow": "0 4px 6px 0 rgba(0, 0, 0, 0.18)",
                        # "margin": "4%",
                        # "width": "10rem",
                        # "height": "3rem",
                        # "text-align": "center",
                        "border": "0px",
}

def create_layout():

    title = html.H2("Attrition Predictor")

    description = html.P("Estimating wich students are at risk of dropping out")

    filters = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Select Entry Year", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-1",
                        options=[
                            {"label": str(year), "value": year}
                            for year in range(2012,2018)
                        ],
                        clearable=True,
                        searchable=False,
                        className="dropdown",
                        style=dropdown_style,
                    ),
                ]
            ),
            html.Div(
                children=[
                    html.Div(children="Select Entry Period", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-2",
                        options=[
                            {"label": str(perios), "value": perios}
                            for perios in range(1,3)
                        ],
                        clearable=True,
                        searchable=False,
                        className="dropdown",
                        style=dropdown_style,
                    ),
                ],
            ),    
            html.Div(
                children=[
                    html.Div(children="Select Treshold", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-3",
                        options=[
                            {"label": th, "value": th}
                            for th in [th/100 for th in range(50,100) if th%5==0]
                        ],
                        clearable=True,
                        className="dropdown",
                        style=dropdown_style,
                    ),
                ]
            ),
            html.Div(
                children=[
                    html.Div(),
                    html.Button(
                        "Predict",
                        id='btn-predict',
                        n_clicks=0,
                        className="buttons",
                        ),
                    
                ],
            ),    
        ],
        className="s-filter-selector",
    )

    table = html.Div(
        children=
        [
            dash_table.DataTable(
                id='data-table',
                # columns=[{"name": i, "id": i} for i in df.columns],
                # data=df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df.columns],
                data=[{}],
                editable=True,
                page_size=10,
                style_cell={
                    "color": "white",
                    "background-color": "#555555",
                    "textAlign": "center",
                },
                style_header={
                    "backgroundColor": "#993737",
                    "color": "white",
                    "textAlign": "center",
                }
            )
        ],
        style={
            # "display": "flex",
            "justify-content": "space-evenly",
            "padding": "24px",
            "margin": "24px",
            # "background-color": "#993737",
        }
    )

    return html.Div(
        [
            title,
            description,
            filters,
            table,
            html.P(id='placeholder')
        ]
    )


@app.callback(Output('placeholder', 'children'),
              Input("filter-1", "value"),
              Input("filter-2", "value"),
              Input("filter-3", "value"))
def update_table_data(year, period, treshold):

    if year:
        table_params['year'] = year
    if period:
        table_params['period'] = period
    if treshold:
        table_params['treshold'] = treshold
    
@app.callback(
    Output('data-table', 'data'),
    Input("btn-predict", "n_clicks"),
    [State("data-table", "data")],
)
def update_table(btn, records):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-predict' in changed_id:

        year = table_params['year']
        period = table_params['period']
        treshold = table_params['treshold']

        if year is None or period is None or treshold is None:
            return [{}]
        
        n, df = predictor.predict(year, period, treshold)

        return df.to_dict('records')