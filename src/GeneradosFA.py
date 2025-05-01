

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
    
    with open (path, "r") as peaks_input:
        #con compresion de listas creamos una lista de una lista por fila del archivo 
        peaks=[(linea.split("\t")) for linea in peaks_input]
        #comoprobar la integridad del archivo de peaks 
        if not peaks: 
            print ("error archivo del peaks vacio")
            exit()
        #Eliminamos el primer elemento de la lista pues es la cabecera del formato tsv
        peaks.pop(0)
        return(peaks)

#carga de los archivos 
input_tsv="C:\\Users\\vrahu\\OneDrive\\Documentos\\Ismadlsh\\CCG\\2025-S2\\Git-Py\\peak_analysis\\data\\union_peaks_file.tsv"
input_genome="C:\\Users\\vrahu\\OneDrive\\Documentos\\Ismadlsh\\CCG\\2025-S2\\Git-Py\\peak_analysis\\data\\E_coli_K12_MG1655_U00096.3.txt"

'''
   Otra alternativa sería: 
   Input_tsv=input("Ingrese la ruta absoluta del archivo tsv")
   Input_genome=input("Ingrese la ruta absoluta del archivo tsv")
    
'''


#Ahora las dos listas genome y peaks tienen la informacion que queremos 
genome=charge_genome(input_genome)
peaks=charge_tsv(input_tsv)

#Creamos un diccionario que contendra todos los TFs como llaves y las posiciones a las que se unen como valores de una lista de tuplas
tf_s={}
#La variable i servira para ir guardando los puntos de union consecutivos que sean iguales siempre ira adelante de los ciclos iterativos
siguiente=1

def write_out (tf):
    '''
    Funcion que crea los archivos de salida por cada TF, recibiendo el diccionario de cada TF 
    y escribiendo las secuencias en un archivo fasta. 
    Parametro: Dic-> Diccionario de TF especifico con las posiciones de salida 
    '''
    #el outputfile se llamara como el TF en cuestion, osea la clave 
    name=next(iter(tf))
    Outputfile=f"TF_{name}.fa"
    #con esta funcion abrimos el archivo a escribir con el protocolo a para reescirbirlo en cada posición 
    with open (Outputfile, "a") as outfile:
            #La cabecera del archivo sera el nombre del TF 
            outfile.write(f">{name}\n")
            #Con el ciclo for vamos haciendo en archivo TF_name.fa , extrayendo todas las posiciones 
            #Por eso el rango correspondiente a la longitud de la lista de tuplas
            for union_site in range(0,len(tf[name])):
                #escribimos el salto de linea para separar cada secuencia
                outfile.write("\n")
                #extraemos cada posicion de inicio y fin 
                inicio=int(tf[name][union_site][0])
                fin=int(tf[name][union_site][1])
                #comprobamos que las posiciones a escribir sean correctas 
                if not inicio or not fin or fin>len(genome):
                    print("error una de las posiciones no existen o esta fuera del rango")
                    exit()
                #escribimos la secuencia referente a la poscion del ciclo for
                #con el metodo join convertimos el slicing de listas en un string 
                outfile.write(f"{tf[name][union_site]}\n{"".join(genome[inicio:fin+1])}")
                
def extraccion_posiciones (tf_extraer):
    '''
    Funcion que extrae todas las posiciones para un TF y las regresa como un diccionario cuya clave es el TF 
    y el valor es una lista de tuplas , cada tupla es un peak de union (inicio, fin)
    Parametro: list-> lista de strings
    Retorna:Dic-> str "nombre" : lista de tuplas
    '''
    #Se guarda el nombre del TF en cuestion 
    tf=tf_extraer[2] 
    #Comprobamos que el TF tenga nombre 
    if tf=="":
        print("error: un TF no cuenta con nombre especificado, este fue ignorado")
        return(0)
    
    #Con compresion de diccionarios se extraen todas las posiciones del TF en cuestion 
    tf_posiciones={tf:[(float(linea[3]), float(linea[4])) for linea in peaks if linea[2]==tf]}
    #Para posibles actualizaciones guardamos el TF y sus posiciones en el diccionario de diccionarios
    tf_s.update(tf_posiciones) 
    #regresamos el diccionario con sus posiciones de union 
    return(tf_posiciones)

#Con este ciclo iterativo logramos sacar todas las posiciones para cada TF dentro de un diccionario 
#la estrategia es ir recorriendo con el segundo if cada linea del arhivo mientras sea del mismo TF
# al encontrar otra con el else en la variable TF_t se guardan todos los sitios de union de ese TF mediante compresion del diccionario 
for linea in peaks: 
    #Por la euristica del algoritmo debemos checar cuando sea la ultima linea esto inidicaria que todos los anteriores o es el ultimo igual por lo que se guarda aparte
    if siguiente == len(peaks):
        tf=extraccion_posiciones(linea)
        siguiente+=1
        write_out(tf)
        break
    #Cuando son iguales seguimos recorriendo la lista con los TF y aumentamos en i para seguiir comparando 
    if linea[2]==peaks[siguiente][2]:
            siguiente+=1
            continue
    #si no se cumple lo anterior significa que todos los recorridos pertenecen a la linea en la iteracion y se guaradan en TF_t y en TFs con la clave como el nombre del TF
    else: 
            tf=extraccion_posiciones(linea)
            siguiente+=1
            write_out(tf)
                    

    

#print(TFs) en TFs es un diccionario con todos los factores de transcripción y sus posiciones 
