import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash
from app import app
import pandas as pd
import plotly.express as px

def build_data():

    cols = ["PERIODO_COHORTE","PERIODO_ACADEMICO","CODIGO","COD_MAT","NOMBRE_MAT","NOTA_DEF","ESTADO"]
    rendimiento_academico = pd.read_csv('data/cleaned/rendimiento_academico.csv')[cols]

    cols = ["FACULTAD", "NOMBRE_PROGRAMA",  "COD_MAT", "NUM_CREDITOS"]
    materias_programa = pd.read_csv('data/cleaned/materias_por_programa.csv')[cols]

    cols = ["COLEGIO_PROCEDENCIA","ES_DESERTOR", "CODIGO", "EDAD", "GENERO", "ENTRY_YEAR"]
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

faculty_opts=[{"label": facultad, "value": facultad}
    for facultad in data.FACULTAD.unique()]
    
program_opts=[{"label": program, "value": program}
    for program in data.NOMBRE_PROGRAMA.unique()]

subject_opts=[{"label": materia, "value": materia}
    for materia in data.NOMBRE_MAT.unique()]

school_opts=[{"label": colegio, "value": colegio}
    for colegio in data.COLEGIO_PROCEDENCIA.unique()]

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
                html.Button("Entry Year", id='btn-year', n_clicks=0, className="buttons"),
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
                    html.Div(
                        children=[
                            html.Div(children="Select Faculty", 
                                        className="filter-title"
                            ),
                            dcc.Dropdown(
                                id="filter-faculty",
                                options=faculty_opts,
                                value=None,
                                clearable=True,
                                # className="dropdown",
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.Div(children="Select Program", className="filter-title"),
                            dcc.Dropdown(
                                id="filter-program",
                                options=program_opts,
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
                                options=subject_opts,
                                value=None,
                                clearable=True,
                                className="dropdown",
                            ),
                        ]
                    ),
                ],
                className="in-selector",
            ),
            html.Div(
                children=[                    
                    html.Div(
                        children=[
                            html.Div(children="Select School", className="filter-title"),
                            dcc.Dropdown(
                                id="filter-school",
                                options=school_opts,
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
                className="in-selector",
            )
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
              Output('filter-faculty', 'options'),
              Output('filter-program', 'options'),
              Output('filter-subject', 'options'),
              Output('filter-school', 'options'),
              Input('btn-grades', 'n_clicks'),
              Input('btn-gender', 'n_clicks'),
              Input('btn-year', 'n_clicks'),
              Input('btn-age', 'n_clicks'),
              Input("filter-faculty", "value"),
              Input("filter-program", "value"),
              Input("filter-subject", "value"),
              Input("filter-school", "value"),
              Input("filter-deserter", "value"))
def update_graph(btn1, btn2, btn3, btn4, faculty, program, subject, school, deserter):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    df = data

    _faculty_opts = faculty_opts
    _program_opts = program_opts
    _subject_opts = subject_opts
    _school_opts = school_opts
    
    if 'btn-grades' in changed_id:
        plot_params['x']="NOTA_DEF"


    ops = options=[{"label": p, "value": p} for p in df.NOMBRE_PROGRAMA.unique()]
    
    if 'btn-grades' in changed_id:
        plot_params['x']="NOTA_DEF"
        plot_params['title']='Final Grade'
    elif 'btn-gender' in changed_id:
        plot_params['x']="GENERO"
        plot_params['title']='Students Gender'
    elif 'btn-year' in changed_id:
        plot_params['x']="ENTRY_YEAR"
        plot_params['title']='Entry Year'

    elif 'btn-age' in changed_id:
        plot_params['x']="EDAD"
        plot_params['title']='Student Attrition by age'

    plot_params['color'] = "ES_DESERTOR" if deserter=='Si' else None

    if faculty:
        df = df[df.FACULTAD == faculty] 
    if program:
        df = df[df.NOMBRE_PROGRAMA == program]
    if subject:
        df = df[df.NOMBRE_MAT == subject]
    if school:
        df = df[df.COLEGIO_PROCEDENCIA == school]

    _faculty_opts=[{"label": facultad, "value": facultad}
        for facultad in df.FACULTAD.unique()]
        
    _program_opts=[{"label": program, "value": program}
        for program in df.NOMBRE_PROGRAMA.unique()]

    _subject_opts=[{"label": materia, "value": materia}
        for materia in df.NOMBRE_MAT.unique()]

    _school_opts=[{"label": colegio, "value": colegio}
        for colegio in df.COLEGIO_PROCEDENCIA.unique()]
    
    plot_params['data'] = df

    chart = px.histogram(plot_params['data'], x=plot_params['x'], color=plot_params['color'], color_discrete_sequence=["#DA7879", "#912F33"], title=plot_params['title'])

    return chart, _faculty_opts ,_program_opts ,_subject_opts ,_school_opts