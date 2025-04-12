
Input_tsv="C:\\Users\\vrahu\\OneDrive\\Documentos\\Ismadlsh\\CCG\\2025-S2\\Git-Py\\peak_analysis\\data\\union_peaks_file.tsv"
Input_genome="C:\\Users\\vrahu\\OneDrive\\Documentos\\Ismadlsh\\CCG\\2025-S2\\Git-Py\\peak_analysis\\data\\E_coli_K12_MG1655_U00096.3.txt"
#abrimos el archivo 
with open (Input_tsv, "r") as Peak_archivo, open (Input_genome, "r") as genome_ecoli:
    Nitrogenadas=list("ATGC")
    Peaks=[(linea.split("\t")) for linea in Peak_archivo] 
    genome=list(genome_ecoli)
    #genome=[char.split("") for char in genome_ecoli if char in Nitrogenadas]

genome_nitro=[]
for linea in genome[1::]: 
    genome_nitro.extend([base for base in linea if base in Nitrogenadas]) 
    
#Ahora las dos listas genome_nitro y genome tienen la informacion que queremos 

#Creamos un diccionario que contendra todos los TFs como llaves y las posiciones a las que se unen como valores de una lista de tuplas
TFs={}
#La variable i servira para ir guardando los puntos de union consecutivos que sean iguales 
i=1
#Eliminamos el primer elemento de la lista pues es la cabecera del formato tsv
Peaks.pop(0)

#Con este ciclo iterativo logramos sacar todas las posiciones para cada TF dentro de un diccionario 
#la estrategia es ir recorriendo con el segundo if cada linea del arhivo mientras sea del mismo TF, al encontrar otra con el else en la variable TF_t se guardan todos los sitios de union de ese TF mediante compresion del diccionario 
for linea in Peaks: 
    #Por la euristica del algoritmo debemos checar cuando sea la ultima linea esto inidicaria que todos los anteriores o es el ultimo igual por lo que se guarda aparte
    if i == len(Peaks):
        TF=linea[2]
        TF_t={TF:[(float(linea[3]), float(linea[4])) for linea in Peaks if TF==linea[2]]}
        TFs.update(TF_t)
        i+=1
        
        Outputfile=f"TF_{TF}.fa"
        with open (Outputfile, "a") as outfile:
                outfile.write(f"{TF}\n")
            #Con el ciclo for vamos haciendo en archivo TF_name.fa 
                for j in range(0,len(TF_t[TF])):
                    outfile.write("\n")
                    inicio=int(TF_t[TF][j][0])
                    fin=int(TF_t[TF][j][1])
                    outfile.write(f"{TF_t[TF][j]}\n{"".join(genome_nitro[inicio:fin+1])}")
        
        #comprobacion de que sirve piola 
        '''
        for j in range(0,len(TF_t[TF])):
            inicio=int(TF_t[TF][j][0])
            fin=int(TF_t[TF][j][1])
            print(f"{TF_t[TF][j]}\n{"".join(genome_nitro[inicio:fin+1])}")
            '''
            
        break
    #Cuando son iguales seguimos recorriendo la lista con los TF y aumentamos en i para seguiir comparando 
    if linea[2]==Peaks[i][2]:
            i+=1
            continue
    #si no se cumple lo anterior significa que todos los recorridos pertenecen a la linea en la iteracion y se guaradan en TF_t y en TFs con la clave como el nombre del TF
    else:
            #La variable TF guarda el nombre del TF en cuestio 
            TF=linea[2]
            #Por compresion de diccionarios obtenemos todas las posiciones de este TF
            TF_t={TF:[(float(linea[3]), float(linea[4])) for linea in Peaks if TF==linea[2]]}
            #metemos este diccionario al diccionario con todos los TFs y sus posiciones 
            TFs.update(TF_t)
            #aumentamos i para seguir en las posiciones en cuestion 
            i+=1
            #La variabel outputfile crea el nombre del archivo de salida por cada TF
            Outputfile=f"TF_{TF}.fa"
            #abrimos el archivo con la variable out file y el metodo with open para a su vez cerrarlo, importante con el metodo a para sobreescribirlo
            with open (Outputfile, "a") as outfile:
                #escribimos primero el nombre del TF
                outfile.write(f">{TF}\n")
            #Con el ciclo for vamos haciendo en archivo TF_name.fa 
                for j in range(0,len(TF_t[TF])):
                    #el salto de linea permite separar cada TF
                    outfile.write("\n")
                    #Las variables guardan como ints las posiciones de cada posicion de union del TF 
                    inicio=int(TF_t[TF][j][0])
                    fin=int(TF_t[TF][j][1])
                    #finalmente escribimos la posicion con slicing de listas el metodo join permite convertir la lista en un string 
                    outfile.write(f"{TF_t[TF][j]}\n{"".join(genome_nitro[inicio:fin+1])}")
                    

    

#print(TFs) en TFs es un diccionario con todos los factores de transcripción y sus posiciones 
