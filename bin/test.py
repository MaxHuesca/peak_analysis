
Nitrogenadas=list("ATGC")
Nitrogenadas[1]="C"
print(Nitrogenadas) 

Secuencia=list("ATGCGTAGC")
print(Secuencia[0:5])
print(Secuencia[:-4:-1])
print(Secuencia[::-1])

Nitrogenadas=list("ATGC")
print(Nitrogenadas)
Frecuencia=[( "A", Secuencia.count("A")), ("T",Secuencia.count("T")), ("G",Secuencia.count("G")), ("C", Secuencia.count("C"))]
print(Frecuencia) 
Frecuencias=[]
for base in Nitrogenadas: 
    Frecuencias.append((base, Secuencia.count(base))) 

print(Frecuencias) 
Secuencia_1=["A", "T", "G", "C", "N", "R", "Y", "A", "T", "G", "C"] 

Secuencia_1=[base for base in Secuencia_1 if base in Nitrogenadas ]
print(Secuencia_1)

for base in Secuencia_1: 
    if base not in Nitrogenadas: 
       Secuencia_1.remove(base) 

print(Secuencia_1) 

Secuencia_2=list("ATGCTTCGAGGG") 

i=0 
ORF_1=[(Secuencia_2[i:i+3])  for i in range(0, len(Secuencia_2),3)]
print(ORF_1)

Secuencia_2=[ "U" if base== "T"else base for base in Secuencia_2  ]
print(Secuencia_2)