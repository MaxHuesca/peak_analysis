"""
Programa que escribe un archivo fasta por cada tf proporcionado con sus secuencias de union 
Imports: 
    -os: permite navegar y alterar los directorios del usuario 

"""
import os
errores=[]

def write_out (tfs, genome):
    '''
    Funcion que crea los archivos de salida por cada TF, recibiendo el diccionario de todos los tfs 
    y escribiendo las secuencias en un archivo fasta. 
    Parametros:
        -tfs (Dic): Diccionario con todos los tfs de un archivo tsv
        -genome (list): lista con todas las bases nitrogenadas de un genoma especifico 
    '''
    direc= os.path.join("output")
    if not os.path.exists(direc):
        os.mkdir(direc)
        print("La carpeta output no existia, se creo una")
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
                    if inicio > fin:
                        pos_temp=inicio
                        inicio=fin
                        fin=pos_temp
                        errores.append(f"Advertencia la posicion {inicio},{fin} del TF {tf} se encontraba en orden inverso ")
                    #comprobamos que las posiciones a escribir sean correctas 
                    if not inicio or not fin or fin>len(genome):
                        outfile.write(f"error la posicion {inicio},{fin} sale del rango del genoma.\n")
                        errores.append(f"La posicion {inicio},{fin} del TF {tf} salió del rango del genoma ")
                        continue
                    #escribimos la secuencia referente a la poscion del ciclo for
                    #con el metodo join convertimos el slicing de listas en un string 
                    outfile.write(f'{union_site} len:{fin-inicio}\n{"".join(genome[inicio:fin])}\n')
    if errores: 
        print("Se detectaron estos errores al procesar los archivos: ")
        for error in errores: 
            print(f"\t-{error}")