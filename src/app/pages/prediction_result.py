import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

gauge_color = {
    'dark':         False,
    'detail':       '#111111',
    'primary':      '#D44646',
    'secondary':    '#9E9E9E'
}

def create_layout():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Button(
                        "Predict",
                        id='btn-features-predict',
                        n_clicks=0,
                        className="buttons",
                    ),   
                ],
                style = {
                    'display':'flex',
                    'justify-content':'space-evenly',
                    'margin': '50px 0 0 0'
                }
            ),
            html.Div(
                daq.DarkThemeProvider(
                    theme = gauge_color,
                    children = [
                        daq.Gauge(
                            id='prediction-gauge',
                            color={"gradient":True,"ranges":{"#00EA64":[0,50],"yellow":[50,80],"#D44646":[80,100]}},
                            size=300,
                            showCurrentValue=True,
                            units="%",
                            min=0,
                            max=100,
                            value=0
                        )
                    ]
                ),                
                style = {
                    'display':'flex',
                    'justify-content':'space-evenly',
                    'margin': '50px 0 0 0'
                }
            )
        ],
        className="predictor-results"
    )