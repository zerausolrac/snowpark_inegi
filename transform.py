#Creación de archivo para transformaciones
from lat_lon_parser import parse
import csv
import gzip
import json
import os

def cleanEmpty(row):
    for i,v in enumerate(row):
        if not v or v == '*':
            row[i] = 'NULL'
        elif v == 'N/D':
            row[i] = 0
        else:
            if str(v):
                row[i] = str(v)
            else:
                if v.isnumeric():
                    row[i] = int(v)
                    print(row[i])
                if float(v):
                    row[i] = float(v)
                    print(row[i])
    return row
     

def openCSV(filename:str):
    newInegi = []
    with open(filename, newline='', encoding='utf8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if not row[0].isnumeric():
                continue
            #mun = 0 (totales de entidad) or loc = 0 (totales de entidad) 
            if int(row[4]) == 0 or int(row[4]) == 9998 or int(row[4]) == 9999:
                continue
            else:
                newRow = [row[0],
                row[2], 
                row[3], 
                row[4], 
                row[5], 
                'NULL' if not row[6] else parse(row[6]), 
                'NULL' if not row[7] else parse(row[7]), 
                row[8],
                row[9],
                row[10], 
                row[11], 
                row[130], 
                row[185], 
                row[186], 
                row[187], 
                row[214], 
                row[215], 
                row[237], 
                row[238],
                row[182]
                ]
                newInegi.append(cleanEmpty(newRow))
    return newInegi



def crearCSV(data):
    csv.register_dialect('pipe', delimiter='|')
    with open('inegi.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f,dialect="pipe")
        for row in data:
            writer.writerow(row)
    f.close()
    print("CSV creado!")




def leerData4Json(archivo:str):
    datos = []
    tempDic = {}
    #Schema de tipos datos
    schema = ['int', 'int', 'str' ,'int','str','float','float','int','int','int','int','int','int','int','int','int','int','int','int','int']
    keys = ['ENTIDAD','MUN','NOM_MUN','LOC','NOM_LOC','LONGITUD','LATITUD','ALTITUD','POBTOT','POBFEM','POBMAS','PCON_DISC','GRAPROES','GRAPROES_F','GRAPROES_M','PSINDER','PDER_SS','VIVTOT','TVIVHAB','VPH_INTER']
    with open(archivo, newline='', encoding='utf8') as file:
        reader = csv.reader(file, delimiter='|', quotechar=',')
        for i,row in enumerate(reader):
            for idx in range((len(row))):
                tempDic[keys[idx]] = validateDatatypeJson(row[idx],schema[idx], i, keys[idx],row)
            datos.append(tempDic)   
            tempDic = {}
    return datos


def validateDatatypeJson(dato, tipo,i, key,row):    
    try:
        if tipo == 'int':
            if dato == 'NULL':
                return 0
            else:
                return int(dato)
        if tipo == 'float':
            if dato == 'NULL':
                return 0.0
            else:
                return float(dato)
        if tipo == 'str':
            if dato == 'NULL':
                return 'NULL'
            else:
                return str(dato)
        else:
            return 'NULL'
    except ValueError as e:
        if key == 'ALTITUD':
            return 0.0
        else:
            return str('******')
        pass
                    




def crearJson(json_filename:str, csv_data):
    with open(json_filename,'w', encoding='utf-8') as jsonfile:
        for row in csv_data:
            jsonfile.write(json.dumps(row) + '\n')
    jsonfile.close()
    print("JSON " + json_filename + " creado!")



def splitJson(csv_data, parts:int):
    dirActual = os.getcwd()
    print(dirActual)
    jsondir = ''
    extractDir = os.path.join(dirActual, 'JSON')
    if not os.path.exists(extractDir):
        os.mkdir(extractDir)
        jsondir = extractDir + '/'
    else:
        jsondir = extractDir + '/'

    idx = 1
    idx_filename = 1
    jsonArray = []
    tregs = len(csv_data)
    rlimits = []
    dranges = []
    print("total registros: " + str(tregs))
    limit = round(tregs // parts) 
    print('limite: ' + str(limit))
    diff = tregs - limit*parts
    print('diferencia: ' + str(diff))
    for i in range(0,parts+1):
        rlimits.append(i*limit)
    
    s = 1
    a = 0

    for i in rlimits:
        if s < len(rlimits): 
            temprange = range(rlimits[a],rlimits[s])
            dranges.append(temprange)
            #json
            filename = jsondir + 'inegi'+ str(idx_filename) + '.json'
            crearJson(filename, csv_data[temprange.start:temprange.stop])
            compressFile(filename)
            idx_filename = idx_filename + 1
            a = s
            s += 1
        elif s == len(rlimits) and diff > 0:
            #json
            filename = jsondir + 'inegi'+ str(idx_filename) + '.json'
            crearJson(filename, csv_data[-diff:])
            compressFile(filename)
            idx_filename = idx_filename + 1
    
    print("JSON particionado!")    
            
    
        


def fullJson(csv_data):
    jsonArray = []
    filename = 'inegi.json'
    for row in csv_data:
        jsonArray.append(row)
    crearJson(filename, jsonArray)
    compressFile(filename)
    print("JSON Completo!")



def compressFile(filename):
    with open(filename, 'rb') as f_in:
        with gzip.open(filename + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)




def totalHabitantesCSV(filename:str):
    total = 0
    with open(filename, newline='',encoding='utf8') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            if row[8].isnumeric():
                total = total + int(row[8])
    file.close()
    return total



def totalHabitantesJson(filename):
    total = 0
    with open(filename, 'r', newline='') as file:
        for row in file:
            datos = json.loads(row)
            #print(datos['POBTOT'])
            total = total + datos['POBTOT']
    file.close()
    return total
