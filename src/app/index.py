import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from pages import demo, visualizacion, datos

sidebar = html.Div(
    [
        html.H2("University of Boyaca", className="display-6"),
        html.Hr(),
        html.P(
            "Analyzing the behavior of student's attrition"
            " in the university of boyaca", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("General", href="/home", active="exact", className="tabs"),
                dbc.NavLink("Prediction", href="/prediction", active="exact", className="tabs"),
                dbc.NavLink("Data", href="/data", active="exact", className="tabs"),
                dbc.NavLink("Visualization", href="/visualization", active="exact", className="tabs"),
                dbc.NavLink("Periods", href="/periods", active="exact", className="tabs"),
            ],
            vertical=True,
            # pills=True,
        ),
    ],
    className="sidebar",
)

content = html.Div(
    id="page-content",
    className="content",
)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar,
        content
    ])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/home":
        return demo.create_layout()
    elif pathname == "/prediction":
        return html.P("Aca va la pagina")
    elif pathname == "/data":
        return datos.create_layout() 
    elif pathname == "/visualization":
        return visualizacion.create_layout()
    elif pathname == "/periods":
        return html.P("Aca va la pagina")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)