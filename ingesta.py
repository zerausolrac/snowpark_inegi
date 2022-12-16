import re
import os
from config import connection_parameters

def solo_archivos(ruta) -> list:
    ingesta_files = []
    for file in os.listdir(ruta):
        # search given pattern in the line 
        if re.search("\.json.gz$", file):
            ingesta_files.append(os.path.join(ruta,file))
    return ingesta_files

def ingesta_setup() -> dict:
    env = {
        'account' : connection_parameters['account'],
        'snowstage' : 'inegi'
    }
    return env


if __name__ == '__main__':
   files = solo_archivos(os.path.join(os.getcwd(),'JSON'))
   print(files)