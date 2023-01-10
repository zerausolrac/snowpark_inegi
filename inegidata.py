import download as d
import transform as t
import os

def urlDownload(tipo:str):
    if tipo == 'remote':    
        url_download = 'https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/iter/iter_00_cpv2020_csv.zip'
        if d.inegiDownloadFile(url_download):
            print('Descargado')
        else:
            print('Ya descargado')   
        d.unzipDatos('iter_00_cpv2020_csv.zip')

    elif tipo == 'local':
        d.unzipLocalDatos('iter_00_cpv2020_csv.zip')
    else:
        return None
    rutaCSV = d.buscarArchivo('conjunto_de_datos_iter_00CSV20.csv')
    newInegi = t.openCSV(rutaCSV)
    t.crearCSV(newInegi)
    newInegi.clear()
    #leer para crear JSON
    leerCSV = t.leerData4Json('inegi.csv')
    t.splitJson(leerCSV,7)
    leerCSV.clear()
    print('Local listo!')