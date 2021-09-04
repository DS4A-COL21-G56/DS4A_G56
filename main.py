from src.app.index import app
import argparse

# Definir argumentos que se pueden especificar por consola
parser = argparse.ArgumentParser(description='baco dash server')

parser.add_argument(
    '-H',
    '--host',
    dest='_run_host',
    action='store_const',
    const=True,
    default=False,
    help='run using "app.run_server(host="0.0.0.0")"'
)

server = app.server

# run the app
if __name__ == '__main__':

    args = parser.parse_args()

    if args._run_host:
        app.run_server(host='0.0.0.0', port=80)
    else:
        app.run_server(debug=True)