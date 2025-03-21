### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA


1.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
2.  **Caso: Archivo de picos vacío.**
    
    -   **Entradas:**
        -   Archivo de picos vacío.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the peak file is empty."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
```

3.  **Caso: Posiciones `Peak_start` y `Peak_end` fuera del rango del genoma.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` fuera del tamaño del genoma.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks are bigger than the genome". Check the log.out file`
        
        -   Generar un archivo de log indicando los picos fuera de rango. El archivo debe contener las líneas del archivo de picos que tienen problemas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
```bash
ls
```

```bash
log.out
fasta_peaks/
```

4. **Que no especifiquen el directorio de salida** 
- **Entradas** 
        -   Archivo de picos 
        -   Archivo FASTA del genoma.
 -   **Esperado:**
        1.  El sistema debe imprimir un mensaje de advertencia: `"Warning: The output file is unspecified, please try again` 
        *Debe haber un exit (1) para volver a correr el script*
        
        2. El sistema manda a un directorio por default 
`"Warning: Because the outfile was Unespecified we sent it to a file in the results directory`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: The output file is unspecified
```

5.  **Caso: Archivo del genoma vacio.**
    
    -   **Entradas:**
        -   Archivo del genoma vacio.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file is empty"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file is empty
    ```

6.  **Caso: Posiciones `Peak_start` y `Peak_end` alguna faltante.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` faltante ya sea una u otra.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks start or end are unespecified". Some output files will be with an error in their peaks`
        -   En los TF que tengfan esta caracteristica en algunos peaks se imprimira el error al generar el archivo fasta y continuara con la siguiente columna

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
 ```
    Error: It have been imposible to determine the end or start of some peaks
 ```

7.  **Caso: TF sin nombre.**
    
    -   **Entradas:**
        -   Archivo de picos.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:**
      -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks do not have name, the program will ignore them`
      -   En los TF que tengan esta caracteristica se ignoraran y continuara con la siguiente linea 


```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: Some TF names were empty, they have been ignore
```
