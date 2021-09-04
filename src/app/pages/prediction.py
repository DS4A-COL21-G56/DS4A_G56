import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import dash
import dash_table
import dash_daq as daq
from src.app import app
import pandas as pd
import plotly.express as px
from src.models import predictor
from . import prediction_board, prediction_result

table_params = dict()
table_params['year'] =      None
table_params['period'] =    None
table_params['treshold'] =  None

features = {
    'n_semesters':          None,
    'cumulative_credits':   None,
    'real_cumulative_gpa':  None,
    'cumulative_failed':    None,
    'gpa_last_semester':    None,
    'GENERO':               None,
    'EDAD':                 None,
    'COLEGIO_PROCEDENCIA':  None,
    'PUNT_TOTAL':           None,
    'PUNT_AREA':            None,
    'FACULTAD':             None,
    'NOMBRE_PROGRAMA':      None
}

dropdown_style =    {
                        "color": "black",
                        "background-color": "#ffffff",
                        "border-radius": "40px",
                        "box-shadow": "0 4px 6px 0 rgba(0, 0, 0, 0.18)",
                        "border": "0px",
}

def create_layout():

    title = html.H1("ATTRITION PREDICTOR", className="tittle")
    description = html.P("Estimating which students were at risk of dropping out at a specific moment in time.")
    
    predictor = html.Div(
                children = [
                    prediction_board.create_layout(),
                    prediction_result.create_layout(),
                ],
                className="s-predictor"
    )

    filters = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Select Year", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-1",
                        options=[
                            {"label": str(year), "value": year}
                            for year in range(2012,2021)
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
                    html.Div(children="Select Period", className="filter-title"),
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
                        id='btn-predict-table',
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
                columns=[{"name": i, "id": i} for i in ['code','semesters','gpa','failed','gender','program','dropout_prob']],
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
            html.Hr(),
            html.H3("Imaginary student"),
            html.P("See how a student's performance affects his or her probability of dropping out."),
            predictor,
            html.Hr(),
            html.H3("From current Data"),
            html.P("Find which students were at risk of dropping out at a specific moment in time."),
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
    Input("btn-predict-table", "n_clicks"),
    [State("data-table", "data")],
)
def update_table(btn, records):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-predict-table' in changed_id:

        year = table_params['year']
        period = table_params['period']
        treshold = table_params['treshold']

        if year is None or period is None or treshold is None:
            return [{}]
        
        n, df = predictor.predictFromDataset(year, period, treshold)

        return df.to_dict('records')

@app.callback(
    dash.dependencies.Output('age-title', 'children'),
    dash.dependencies.Output('nsemesters', 'children'),
    dash.dependencies.Output('last-gpa', 'children'),
    dash.dependencies.Output('gpa', 'children'),
    dash.dependencies.Input('gender-radio', 'value'),
    dash.dependencies.Input('age-slider', 'value'),
    dash.dependencies.Input('faculty-filter-1', 'value'),
    dash.dependencies.Input('program-filter-1', 'value'),
    dash.dependencies.Input('school-filter-1', 'value'),
    dash.dependencies.Input('icfes-input', 'value'),
    dash.dependencies.Input('icfes-area-input', 'value'),
    dash.dependencies.Input('semesters-slider', 'value'),
    dash.dependencies.Input('cumulative-credits-input', 'value'),
    dash.dependencies.Input('failed-credits-input', 'value'),
    dash.dependencies.Input('last-gpa-input', 'value'),
    dash.dependencies.Input('cumulative-gpa-input', 'value'),
)
def update_inputs ( gender, age, faculty, program, school, icfes, area,
                    semesters, totalcredits, failedcredits, lastgpa, gpa):
    
    if gender:
        features['GENERO'] = [gender]
    if age:
        features['EDAD'] = [age]
    if faculty:
        features['FACULTAD'] = [faculty]
    if program:
        features['NOMBRE_PROGRAMA'] = [program]
    if school:
        features['COLEGIO_PROCEDENCIA'] = [school]
    if icfes:
        features['PUNT_TOTAL'] = [icfes]
    if area:
        features['PUNT_AREA'] = [area]
    if semesters:
        features['n_semesters'] = [semesters]
    if totalcredits:
        features['cumulative_credits'] = [totalcredits]
    if failedcredits:
        features['cumulative_failed'] = [failedcredits]
    if lastgpa:
        features['gpa_last_semester'] = [lastgpa]
    if gpa:
        features['real_cumulative_gpa'] = [gpa]
    
    return  (
        f"Age: {age}", 
        f"# Finished semesters: {semesters}",
        f"Last semester GPA: {lastgpa}",
        f"cumulative GPA: {gpa}"
    )

@app.callback(
    Output('prediction-gauge', 'value'),
    Input("btn-features-predict", "n_clicks"),
)
def update_gauge(btn):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-features-predict' in changed_id:

        p = predictor.predictFromFeatures(features)

        print(p)

        return p