"""
Programa que ejecuta el script para leer y escribir los archivos de analisis de chip seq
utiliza los modulos hechos para cada tarea especifica: 

Imports: 
    -charge_genome: funcion que permite la carga del genoma 
    -charge_tsv:  funcion que permite la lectura del archivo tsv
    -write_out: funcion que crea todos los archivos fasta uno por cada tf
    -os: paqueteria que permite manipular y usar los directorios 
"""

import os
import argparse 
from read_genome import charge_genome
from read_tsv import charge_tsv
from writes_fastas import write_out


def main():
    #parseador: 
    #Creamos el objeto parseador 
    parser= argparse.ArgumentParser(description="Parser para guardar los argumentos")
    #Creamos todos lo argumentos necesarios para el programa
    parser.add_argument("--tsv", default="E_coli_K12_MG1655_U00096.3.txt", hepl="Especifica el nombre del archivo tsv")
    parser.add_argument("--fasta", default="union_peaks_file.tsv", hepl="Especifica el nombre del archivo fasta")
    #obtenemos los argumentos en una variable 
    args= parser.parse_args()
    
    #carga de los archivos, ruta proporcionada por el usuario 
    path=args.tsv
    input_tsv=os.path.join("data", path)
    #Nos aseguramos que el archivo exista
    if not os.path.exists(input_tsv):
        print(f"Error: el archivo {input_tsv} no existe.")
        exit(1)
    path=args.fasta
    input_genome=os.path.join("data", path)
    #Nos aseguramos que el archivo exista
    if not os.path.exists(input_genome):
        print(f"Error: el archivo {input_genome} no existe.")
        exit(1)
        
    #Ahora las dos listas genome y peaks tienen la informacion que queremos 
    genome=charge_genome(input_genome)
    tfs=charge_tsv(input_tsv)
    
    #Escribimos cada archivo con la funcion write out 
    write_out(tfs,genome)
    #Le damos el mensaje al usuario de que fueron creados sin ningun error
    print("Los archivos fueron creados con exito y guardados en la carpeta de output")

   
if __name__ == "__main__":
	main()