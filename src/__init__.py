from os import path

# path absoluto al direcotrio de la aplicacion:
abs_path = path.dirname(path.realpath(__file__))
abs_path = '/'.join(abs_path.split(path.sep)).split("src")[0]