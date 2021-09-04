import dash
import dash_bootstrap_components as dbc

# import flask
# import glob
# import os

# image_directory = os.getcwd() + "/src/app/assets/img/"
# list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
# static_image_route = '/static/'

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title = "UBoyaca: attrition"

# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
# @app.server.route('{}<image_path>.png'.format(static_image_route))
# def serve_image(image_path):
#     image_name = '{}.png'.format(image_path)
#     if image_name not in list_of_images:
#         raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
#     return flask.send_from_directory(image_directory, image_name)