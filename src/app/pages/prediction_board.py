import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from .visualizacion import faculty_opts, program_opts, school_opts

knob_color = {
    'dark': False,
    'detail': '#9E9E9E',
    'primary': '#f57979',
    'secondary': '#9E9E9E'
}

dropdown_style =    {
    'font-size': 'x-small',
    "color": "black",
    "background-color": "#ffffff",
    "border-radius": "40px",
    "box-shadow": "0 4px 6px 0 rgba(0, 0, 0, 0.18)",
    "border": "0px",
    "width": "100%"
}

def create_layout():
    
    gender_age = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(id='gender', children="Gender:"),
                    dcc.RadioItems(
                        id='gender-radio',
                        options=[
                            {'label': 'F', 'value': 'F'},
                            {'label': 'M', 'value': 'M'},
                        ],
                        value='F',
                        labelStyle={'display': 'inline-block', 'width':'40px'}
                        # labelStyle={'display': 'block'}
                    )
                ],
                style={'width':'20%'}
            ),
            html.Div(
                children=[
                    html.Div(id='age-title', children="Age:"),
                    dcc.Slider(
                        id='age-slider',
                        min=16, max= 60, step=1, value=16,
                        marks={i: str(i) for i in range(20,61,10)},
                        className='slider'
                    )
                ],
                style={'width':'80%'}
            ),
        ],
        style = {'display':'flex', 'justify-content':'space-evenly'}
    )

    faculty_program = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Faculty"),
                    dcc.Dropdown(
                        id="faculty-filter-1",
                        options=faculty_opts,
                        clearable=True,
                        searchable=False,
                        style=dropdown_style,
                    )
                ],
                style={'width':'40%'}
            ),
            html.Div(
                children=[
                    html.Div(children="Program"),
                    dcc.Dropdown(
                        id="program-filter-1",
                        options=program_opts,
                        clearable=True,
                        searchable=False,
                        style=dropdown_style,
                    )
                ],
                style={'width':'40%'}
            ),   

        ],
        style = {
            'display':'flex',
            'justify-content':'space-evenly',
            'margin':'5% 0 0 0'    
        }
    )
    
    school = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Origin School:"),
                    dcc.Dropdown(
                        id="school-filter-1",
                        options=school_opts,
                        clearable=True,
                        searchable=False,
                        style=dropdown_style,
                    )
                ],
                style={'width':'25%'}
            ),
            html.Div(
                children=[
                    html.Div(children="Icfes Score:"),
                    daq.NumericInput(
                        id='icfes-input',
                        min=0,
                        max=500,
                        value=0
                    ),
                    # dcc.Dropdown(
                    #     id="filter-2",
                    #     options=[
                    #         {"label": str(score), "value": score}
                    #         for score in range(0,101)
                    #     ],
                    #     clearable=True,
                    #     searchable=False,
                    #     style=dropdown_style,
                    # )
                ],
                style={'width':'25%'}
            ),   
            html.Div(
                children=[
                    html.Div(children="Icfes Area Score:"),
                    daq.NumericInput(
                        id='icfes-area-input',
                        min=0,
                        max=500,
                        value=0
                    ),
                    # dcc.Dropdown(
                    #     id="filter-2",
                    #     options=[
                    #         {"label": str(score), "value": score}
                    #         for score in range(0,101)
                    #     ],
                    #     clearable=True,
                    #     searchable=False,
                    #     style=dropdown_style,
                    # )
                ],
                style={'width':'25%'}
            ),   
        ],
        style = {
            'display':'flex',
            'justify-content':'space-evenly',
            'margin':'5% 0 0 0'    
        }
    )

    semesters = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(id='nsemesters', children="# Finished semesters:"),
                    dcc.Slider(
                        id='semesters-slider',
                        min=0, max= 20, step=1, value=0,
                        marks={i: str(i) for i in range(0,21,5)},
                        className='slider'
                    )
                ],
                style = {'width':'60%'}
            ),
            html.Div(
                [
                    # html.Div("Credits:"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div("Taken"),
                                    html.Div("credits"),
                                    daq.NumericInput(
                                        id='cumulative-credits-input',
                                        min=0,
                                        max=300,
                                        value=0
                                    ),
                                ],
                                style = {'width':'50%'}
                            ),
                            html.Div(
                                [
                                    html.Div("Failed"),
                                    html.Div("subjects"),
                                    daq.NumericInput(
                                        id='failed-credits-input',
                                        min=0,
                                        max=100,
                                        value=0
                                    ),
                                ],
                                style = {'width':'50%'}
                            )
                        ],
                        style={'display':'flex', 'justify-content':'space-evenly'}
                    )
                ],
                style = {'width':'40%'}
            )
        ],
        style = {
            'display':'flex',
            'justify-content':'space-evenly',
            'margin':'5% 0 0 0'
        }
    )    

    gpa = daq.DarkThemeProvider(
        theme = knob_color,
        children=[
            html.Div(
                children=[ 
                    html.Div(
                        children = [
                            html.Div(id='last-gpa', children="Last semester GPA:"),
                            daq.Knob(
                                id='last-gpa-input',
                                size=150,
                                min=0,
                                max=5,
                                value=3.5,
                                # style={'background-color':'green'}
                            )
                        ]
                    ),
                    html.Div(
                        children = [
                            html.Div(id='gpa', children="cumulative GPA:"),
                            daq.Knob(
                                id='cumulative-gpa-input',
                                size=150,
                                min=0,
                                max=5,
                                value=3.5
                            )
                        ]
                    ),
                ],
                style = {
                    'display':'flex',
                    'justify-content':'space-evenly',
                    'margin':'5% 0 0 0'
                }
            )
        ]
    )
        
    return html.Div(
        children=[
            gender_age,
            faculty_program,
            school,
            semesters,
            gpa
        ],
        className="predictor-inputs"
    )