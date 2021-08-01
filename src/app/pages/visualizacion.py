import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash
from app import app
import pandas as pd
import plotly.express as px

def build_data():

    rendimiento_academico = pd.read_csv('data/cleaned/rendimiento_academico.csv')

    cols = ["FACULTAD", "NOMBRE_PROGRAMA",  "COD_MAT", "NUM_CREDITOS"]
    materias_programa = pd.read_csv('data/cleaned/materias_por_programa.csv')[cols]

    cols = ["COLEGIO_PROCEDENCIA","ES_DESERTOR", "CODIGO", "EDAD","GENERO"]
    perfil_ingreso = pd.read_csv('data/cleaned/perfil_ingreso_v2.csv')[cols]

    data = perfil_ingreso[perfil_ingreso.COLEGIO_PROCEDENCIA != 'universidad']
    data = data.merge(rendimiento_academico, left_on='CODIGO', right_on='CODIGO')
    data = data.merge(materias_programa, left_on='COD_MAT', right_on='COD_MAT')

    return data

data = build_data()

# Initial plot parameters
plot_params = {
    'data':data,
    'x':"NOTA_DEF",
    'color':"ES_DESERTOR",
    'title':'Final Grade'
}

# df = pd.read_csv('data/cleaned/perfil_ingreso_v2.csv')
# cols = ["COLEGIO_PROCEDENCIA","ES_DESERTOR", "CODIGO", "EDAD","GENERO"]
# data = df[df.COLEGIO_PROCEDENCIA != 'universidad'][cols]

# data2 = pd.read_csv('data/cleaned/rendimiento_academico.csv')["NOTA_DEF"]

def create_layout():

    buttons = html.Div(
        [
            html.H2("Visualization", className="display-5"),
            html.Div([
                html.Button("Grades", id='btn-grades', n_clicks=0, className="buttons"),
                html.Button("Gender", id='btn-gender', n_clicks=0, className="buttons"),
                html.Button("High school", id='btn-school', n_clicks=0, className="buttons"),
                html.Button("Age", id='btn-age', n_clicks=0, className="buttons"),
                ]
            )
        ]
    )

    visualization = html.Div(
        children=dcc.Graph(
            id="visualization-content", config={"displayModeBar": False},
        ),
    )

    filters = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Select Faculty", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-faculty",
                        options=[
                            {"label": facultad, "value": facultad}
                            for facultad in data.FACULTAD.unique()
                        ],
                        value=None,
                        clearable=True,
                        className="dropdown",
                    ),
                ]
            ),
            html.Div(
                children=[
                    html.Div(children="Select Program", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-program",
                        options=[
                            {"label": program, "value": program}
                            for program in data.NOMBRE_PROGRAMA.unique()
                        ],
                        value=None,
                        clearable=True,
                        className="dropdown",
                    ),
                ],
            ),    
            html.Div(
                children=[
                    html.Div(children="Select Subject", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-subject",
                        options=[
                            {"label": materia, "value": materia}
                            for materia in data.NOMBRE_MAT.unique()
                        ],
                        value=None,
                        clearable=True,
                        className="dropdown",
                    ),
                ]
            ),
            html.Div(
                children=[
                    html.Div(children="View Deserters?", className="filter-title"),
                    dcc.Dropdown(
                        id="filter-deserter",
                        options=[
                            {"label": "Si", "value": "Si"},
                            {"label": "No", "value": "No"},
                        ],
                        value="Si",
                        className="dropdown",
                    ),
                ],
            ),    
        ],
        className="filter-selector",
    )


    return html.Div(
        [
            buttons,
            visualization,
            filters,
        ])

def filer(df, faculty=None, program=None, subject=None):
    if faculty:
        df = df[df.FACULTAD == faculty] 
    if program:
        df = df[df.NOMBRE_PROGRAMA == program]
    if subject:
        df = df[df.NOMBRE_MAT == subject]
    
    return df

@app.callback(Output('visualization-content', 'figure'),
              Input('btn-grades', 'n_clicks'),
              Input('btn-gender', 'n_clicks'),
              Input('btn-school', 'n_clicks'),
              Input('btn-age', 'n_clicks'),
              Input("filter-faculty", "value"),
              Input("filter-program", "value"),
              Input("filter-subject", "value"),
              Input("filter-deserter", "value"))
def update_graph(btn1, btn2, btn3, btn4, faculty, program, subject, deserter):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-grades' in changed_id:
        plot_params['x']="NOTA_DEF"
        plot_params['title']='Final Grade'
    elif 'btn-gender' in changed_id:
        plot_params['x']="GENERO"
        plot_params['title']='Students Gender'
    elif 'btn-school' in changed_id:
        plot_params['x']="COLEGIO_PROCEDENCIA"
        plot_params['title']='Origin High School'
    elif 'btn-age' in changed_id:
        plot_params['x']="EDAD"
        plot_params['title']='Student Attrition by age'

    plot_params['color'] = "ES_DESERTOR" if deserter=='Si' else None

    df = data

    if faculty:
        df = df[df.FACULTAD == faculty] 
    if program:
        df = df[df.NOMBRE_PROGRAMA == program]
    if subject:
        df = df[df.NOMBRE_MAT == subject]
    
    plot_params['data'] = df

    return px.histogram(plot_params['data'], x=plot_params['x'], color=plot_params['color'], color_discrete_sequence=["#DA7879", "#912F33"], title=plot_params['title'])