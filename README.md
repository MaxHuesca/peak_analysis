<h1 align="center">Proyecto de automatizacion de extractor de secuencias de transcription factors factors en E. coli</h1>

## Contenidos: 
1. Resumen
2. Datos disponibles
3. Objetivos
4. Uso 
5. Buenas practicas
6. Plan de Implementación
7. Licencia

## Resumen: 

Este proyecto pretente implementar al extraccion automatica de secuencias de union de dsitintos TFs mediante dos archivos, uno fasta y un tabular, para de esta forma
generar un archivo fasta por TF con sus sitios de union y secuencia, para poder automatizar el uso del software meme en bash 

## Datos disponibles 

### Archivos de picos 

Contiene información sobre las regiones de unión de los 144 factores de transcripción. Se organiza en las siguientes columnas:

- **Dataset_Ids**: Identificadores de los datasets. Cada identificador representa un experimento o condición específica bajo la cual se identificaron los sitios de unión para el TF correspondiente.
- **TF_name**: Nombre del factor de transcripción que se une a la secuencia de ADN especificada.
- **Peak_start**: Posición inicial del pico de unión en el genoma.
- **Peak_end**: Posición final del pico de unión en el genoma.
- **Peak_center**: Posición central del pico de unión en el genoma.
- **Peak_number**: Número secuencial del pico, útil para referencias internas dentro del mismo conjunto de datos.
- **Max_Fold_Enrichment**: Enriquecimiento máximo observado en el pico.
- **Max_Norm_Fold_Enrichment**: Enriquecimiento máximo normalizado.
- **Proximal_genes**: Genes próximos al sitio de unión.
- **Center_position_type**: Tipo de posición central del pico (por ejemplo, intergénica, intrónica, etc.).

`data\union_peaks_file.tsv`

### Genoma Completo de E. coli

Disponible todo el genoma de escherechia coli k12 en formato FASTA. 
`data\E_coli_K12_MG1655_U00096.3.txt`

### Archivos de prueba 

- `data\genoma_vacio`: archivo con el genoma de E. coli vacio para manejo de errores
- `data\peaks_vacio`: archivo de tsv de picos vacio para manejo de errores
- `data\prueba_genoma.txt`: archivo fasta con el genoma parcial de E. coli para prueba *archivo default del argumento --fasta**
- `data\prueba_tsv.tsv`: archivo tsv con errores en las posiciones de los tfs *archivo deafult del argumento --tsv**

## Objetivo  

### Generación de Archivos FASTA
Desarrollar un programa que extraiga y compile las secuencias de picos para cada TF en archivos individuales en formato FASTA. Cada archivo representará un regulador específico.
Este programa implementado en python como un CLI (comand line interface), genera todos los archivos en una carpeta **output** 

```bash
$ python .\src\main.py --fasta E_coli_K12_MG1655_U00096.3.txt --tsv union_peaks_file.tsv
```

> Sus parametos por default permite visualizar el funcionamiento del programa a baja escala y algunos manejos de errores :
> ```bash
> $ python .\src\main.py
> $ La carpeta output no existia, se creo una
> $ Se detectaron estos errores al procesar los archivos: 
> $       -Advertencia la posicion 17096,18945 del TF aaeR se encontraba en orden inverso
> $       -La posicion 3374465,3374895 del TF aaeR salió del rango del genoma
> $       -La posicion 3898492,3898787 del TF csgD salió del rango del genoma
> $ Los archivos fueron creados con exito y guardados en la carpeta de output
> 
> ```

## Uso 

- **Importante contar con pandas instalado en su entorno de python** 

```bash
pip install pandas
```

- **Descargar src y data para funcionamiento minimo del programa en la estructura propuesta** 

- **Run del programa en el directorio padre de src y data**
```bash
peak_analisis/
├── src/                  # Scripts ejecutables principales
│   └── main.py
│   └── read_genome.py
│   └── read_tsv.py
│   └── writes_fastas.py
├── data/                  # Datos para correr el programa 
│   └── E_coli_K12_MG1655_U00096.3.txt
│   └── union_peaks_file.tsv
│   └── prueba_tsv.tsv
│   └── prueba_genoma.txt
├── doc/               # Archivos de documentacion
│   └── Detalles proyecto.md
│   └── Pruebas.md
├── results/               
├── README.md             # Documentación general del proyecto
├── LICENSE               # Licencia del proyecto
└── .gitignore            # Exclusiones para Git
```

  

## Buenas Prácticas de Desarrollo

Para asegurar la calidad y mantenibilidad del software, el proyecto seguirá estas buenas prácticas:

- **Control de Versiones**: Uso de Git para el control de versiones, asegurando una gestión eficaz de los cambios y la colaboración.
- **Revisión de Código**: Implementación de revisiones de código periódicas para mejorar la calidad del software y compartir conocimientos entre el equipo.
- **Documentación Exhaustiva**: Mantener una documentación completa tanto del código como de los procesos operativos, asegurando que cualquier nuevo colaborador pueda integrarse fácilmente.
- **Pruebas Automatizadas**: Desarrollo de pruebas automatizadas para validar la funcionalidad y robustez del software.

## Plan de Implementación

1. **Desarrollo del Extractor de Secuencias**: Programación de la tarea que consiste en genera los archivos FASTA a partir del archivo de picos. Como es un proceso automatizado, todos la información requerida para ejecutar los programas debe ser por línea de comandos.
2. **Integración y Pruebas**: Combinación de los módulos desarrollados y realización de pruebas integrales para asegurar la funcionalidad.

## Licencia  

Ver el archivo `Licensce.txt` para la informacion completa de la licencia 
