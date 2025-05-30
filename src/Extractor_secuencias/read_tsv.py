"""
Programa aque ayuda a leer cualquier archivo tsv de union de TFs y extraer las posiciones de union 
Imports: 
    -panda : paqueteria que permite leer el tsv y manipularlo como un dataframe
"""

import pandas as pd
def charge_tsv (path): 
    '''
    Funcion que carga el archivo tsv correspondiente a los picos de union y lo devuelve 
    como un diccionario donde cada clave es un TF y cada valor es una lista de tuplas
    con las posiciones de union
    Parametros: 
        -path (string): indica la direccion en el que se encuentra el archivo de tsv
    Returns:
        -dic  (dicionario): diccionario con todos los tfs y sus sitios de union 
    '''
    #Creamos un data frame con pandas del archivo tsv
    try:
        peaks_pd=pd.read_csv(
        path,
        sep="\t",
        header=0, 
        ) 
    except Exception: 
        raise ValueError("El archivo proporcionado no cuenta con un formato adecuado asegurese que sea tabular")
    #Solo obtenemos los nombres de los peaks y las posiciones de union
    peaks_df=peaks_pd[["TF_name","Peak_start","Peak_end"]]
    #Lo convertimos en un diccionario 
    dic={
    tf:list(zip(group["Peak_start"],group["Peak_end"]))
    for tf,group in peaks_df.groupby("TF_name")
    }
    return(dic)
