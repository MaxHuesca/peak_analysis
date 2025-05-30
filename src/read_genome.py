"""
Programa que permite leer un archivo fasta cpn todo un genoma completo y devolver una lista 
con todos las bases ntrogendas en el
"""

def charge_genome (path):
    '''
    Funcion que cargar el archivo fasta especificado por una path y lo devuelve como una 
    lista con todas sus bases nitrogenadas como elemento 
    Parametro: 
        path (string):ruta del archivo
    Returns:
        genome_nitro (list): lista de strings con todas las bases del genoma
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