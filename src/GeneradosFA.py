
"""


"""
import os 
import pandas as pd
def charge_genome (path):
    '''
    Funcion que cargar el archivo geenbank especificado por una path y lo devuelve como una 
    lista con todas sus bases nitrogenadas como elemento 
    parametro: str-> ruta del archivo
    retorna: list-> lista de strings 
    '''
    with open (path, "r") as genome_input:
        genome=list(genome_input)
        #si el archivo proporcionado no es aquel con las bases 
        if not genome: 
            print ("error archivo del genoma vacio")
            exit()
        #lista para combrobar que todos los caracteres son bases nitrogenadas 
        nitrogenadas=list("ATGC")
        #lista que alvergara temporalmente el genoma 
        genome_nitro=[]
        #con este ciclo for tomamos todas las lineas del archivo de genoma excepto la primera con la informacion 
        for linea in genome[1::]: 
            #extendemos la linea por cada base comprobada
            genome_nitro.extend([base for base in linea if base in nitrogenadas]) 
            
        return(genome_nitro)
            
def charge_tsv (path): 
    '''
    Funcion que carga el archivo tsv correspondiente a los picos de union y lo devuelve 
    como una lista de listas de strings, cada lista interna corresponde a un TF y cada string
    una columna del tabular, se elimina la primer fila por logistica
    parametro: str-> ruta del archivo 
    retorna: list -> lsita de listas de strings 
    '''
    #Creamos un data frame con pandas
    peaks_pd=pd.read_csv(
    path,
    sep="\t",
    header=0, 
    )
    #Solo obtenemos los nombres de los peaks y las posiciones de union
    peaks_df=peaks_pd[["TF_name","Peak_start","Peak_end"]]
    
    return(peaks_df)

def extraccion_posiciones (peaks):
    '''
    Funcion que extrae todas las posiciones para un TF y las regresa como un diccionario cuya clave es el TF 
    y el valor es una lista de tuplas , cada tupla es un peak de union (inicio, fin)
    Parametro: list-> lista de strings
    Retorna:Dic-> str "nombre" : lista de tuplas
    '''
    #Creamos un diccionario como llave cada tf y clave todas sus posiciones de union  
    tf_dc={
    tf:list(zip(group["Peak_start"],group["Peak_end"]))
    for tf,group in peaks.groupby("TF_name")
    }
    return tf_dc


def write_out (tfs, genome):
    '''
    Funcion que crea los archivos de salida por cada TF, recibiendo el diccionario de cada TF 
    y escribiendo las secuencias en un archivo fasta. 
    Parametro: Dic-> Diccionario de TF especifico con las posiciones de salida 
    '''
    direc= os.path.join("..", "results")
    if not os.path.exists(direc):
        os.mkdir(direc)
        print("La carpeta results no existia, se creo una")
    #Hacemos la iteracion de cada clave dentro del diccionario
    for tf in tfs: 
        #el nombre del archivo sera el de la clave del diccionario con todos los tf 
        outputfile=os.path.join(direc, f"{tf}.fa")
        #con esta funcion abrimos el archivo a escribir con el protocolo a para reescirbirlo en cada posición 
        with open (outputfile, "w") as outfile:
                #La cabecera del archivo sera el nombre del TF 
                outfile.write(f">{tf} union sites\n")
                #Con el ciclo for vamos haciendo en archivo name.fa , extrayendo todas las posiciones 
                #Por eso el rango correspondiente a la longitud de la lista de tuplas
                for union_site in tfs[tf]:
                    #escribimos el salto de linea para separar cada secuencia
                    outfile.write("\n")
                    #extraemos cada posicion de inicio y fin 
                    inicio=int(union_site[0])
                    fin=int(union_site[1])
                    #comprobamos que las posiciones a escribir sean correctas 
                    if not inicio or not fin or fin>len(genome):
                        print("error una de las posiciones no existen o esta fuera del rango, fue ignorada")
                        continue
                    #escribimos la secuencia referente a la poscion del ciclo for
                    #con el metodo join convertimos el slicing de listas en un string 
                    outfile.write(f'{union_site} len:{fin-inicio}\n{"".join(genome[inicio:fin+1])}')
                

def main():
        
    #carga de los archivos, ruta proporcionada por el usuario 
    path=input("Ingrese el nombre de su archivo tsv en su carpeta data:")
    input_tsv=os.path.join("..", "data", path)
    if not os.path.exists(input_tsv):
        print(f"Error: el archivo {input_tsv} no existe.")
        exit(1)
    path=input("Ingrese el nombre de su archivo fasta en su carpeta data:")
    input_genome=os.path.join("..", "data", path)
    if not os.path.exists(input_genome):
        print(f"Error: el archivo {input_genome} no existe.")
        exit(1)
    #Ahora las dos listas genome y peaks tienen la informacion que queremos 
    genome=charge_genome(input_genome)
    peaks=charge_tsv(input_tsv)

    #creamos el diccionario con todos los tf y sus posiciones de union 
    tfs=extraccion_posiciones(peaks)
    #Escribimos cada archivo con la funcion write out 
    write_out(tfs,genome)
    #Le damos el mensaje al usuario de que fueron creados sin ningun error
    print("Los archivos fueron creados con exito y guardados en la carpeta de results")

   
if __name__ == "__main__":
	main()
 

    

