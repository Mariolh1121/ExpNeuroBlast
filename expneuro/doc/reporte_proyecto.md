# Análisis de expresión del gen MOX_1
# Análisis de expresión diferencial del gen MOXD1 durante el desarrollo embrionario de Gallus gallus 

Nombre: Mario Alberto Limón Hernández mariolh@lcg.unam.mx
Nombre: Silvana Yalu Cristo Martinez silavanac@lcg.unam.mx
Nombre: Silvana Yalú Cristo Martínez silvanac@lcg.unam.mx

Fecha:  10/09/2024


## Introducción

El neuroblastoma es uno de los tipos de cáncer más comunes en la infancia, derivado de células de la cresta neural, una población celular que da origen a diversos tipos de tejidos durante el desarrollo embrionario temprano. Estas células son extremadamente plásticas y pueden diferenciarse en neuronas, células gliales, melanocitos y células de la médula adrenal, entre otras. La disregulación genética en esta población celular es un factor clave en la oncogénesis del neuroblastoma.

Un gen que ha mostrado estar fuertemente relacionado con la progresión del neuroblastoma es MOXD1. Este gen, asociado al metabolismo de iones de cobre y al desarrollo de las glándulas suprarrenales, ha sido recientemente identificado como un posible supresor tumoral en neuroblastoma, sin embargo, su papel en el desarrollo embrionario en general y su implicación en el establecimiento de rutas de señalización cruciales, como las involucradas en la diferenciación neural y la homeostasis de metales, sigue siendo poco conocido.

Recientes estudios, como el trabajo de Fredlund et al. (2023) publicado en Science Advances, han investigado el papel de MOXD1 utilizando múltiples organismos modelo, incluidos ratones y pollos (Gallus gallus). En su investigación, los autores demostraron que la disrupción de MOXD1 provoca un desarrollo embrionario anormal, lo cual refuerza su papel regulador en procesos cruciales como el desarrollo de la glándula adrenal y en la progresión de tumores neuroblásticos. Estos hallazgos sugieren que MOXD1 tiene una función crítica en mantener el equilibrio adecuado de la señalización celular durante la diferenciación.

Este proyecto se centrará en investigar cómo la eliminación de MOXD1 mediante un enfoque de knockout en Gallus gallus afecta la expresión génica a nivel global, con un enfoque particular en las rutas relacionadas con el desarrollo, el metabolismo de iones de cobre y la progresión del cáncer. Para ello, se llevará a cabo un análisis de expresión diferencial utilizando datos de RNA-seq, lo que permitirá identificar genes que cambian su nivel de expresión en respuesta a la pérdida de MOXD1. Posteriormente, se realizarán análisis de enriquecimiento funcional para explorar qué rutas biológicas se ven más afectadas en este contexto.

A través de este estudio, se espera avanzar en la comprensión del papel de MOXD1 en el desarrollo embrionario y su posible conexión con el neuroblastoma, con implicaciones para futuras investigaciones sobre la prevención y tratamiento de esta enfermedad.

## Planteamiento del problema

El neuroblastoma es un cáncer infantil derivado de células de la cresta neural que sigue siendo una de las principales causas de muerte por cáncer en la infancia. A pesar de los avances en el tratamiento, los mecanismos moleculares que regulan la progresión de este cáncer y su relación con el desarrollo embrionario normal aún no se comprenden completamente. MOXD1 ha sido identificado como un gen supresor tumoral en el neuroblastoma, pero su papel exacto en el desarrollo embrionario, especialmente en procesos clave como el metabolismo de iones de cobre y la diferenciación de tejidos derivados de la cresta neural, sigue sin estar claro.

El knockout de MOXD1 en Gallus gallus ofrece una oportunidad única para investigar cómo su eliminación afecta el desarrollo, así como su conexión con vías biológicas críticas. La falta de comprensión sobre estas vías específicas es un obstáculo para el desarrollo de terapias dirigidas más efectivas contra el neuroblastoma y otras enfermedades relacionadas. Este proyecto busca abordar esta brecha, explorando los efectos de la disrupción de MOXD1 en la expresión génica y las rutas biológicas durante el desarrollo embrionario.
 


## Metodología

Los datos fueron descargados de GEO en NCBI del siguiente link: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700
Los archivos se encuentran en la carpeta data:
| -- data
|   | -- GSE242700_2020_75_R2_gene_id.featureCounts.tsv
|   | -- GSE242700_family.soft

<!-- [Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.]


### A. Servidor y software

> Servidor: 

> Usuario: 

> Software: 

### B. Datos de Entrada 


```
-->

#### Metadatos de la carpeta de datos
GEO access: GSE242700
Fecha de descarga: 17/09/2024

| Archivo                                           | Descripción                                         | Tipo |
|:--      |:--           |:--  |
|  GSE242700_2020_75_R2_gene_id.featureCounts.tsv   | Archivo de los datos de expresión con el knockout del gen *MOXD1* | tsv | 
|  GSE242700_family.soft   | Archivo con la información del experimento, y sus adheciones de cada condición | soft |
<!-- 


>| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| coli_genomic.fna  | Secuencia de nucleotidos de E. coli  | Formato FastA |
| coli.gff.   | Anotación del genoma de E. coli  | Formato gff |
| coli_protein.faa | Secuencia de aminoacidos de las proteinas de E. coli | formato FastA|
| flagella_genes.txt | Genes con función relacionada al flagello en E. coli | lista |
| directorio.txt. | Archivo con nombres de personas | lista |

-->

#### Formato de los archivos


- `coli_genomic.fna` : formato FastA


```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG
GTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGAC
AGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
```

Formato: 

> a. La primera línea es información de la secuencia. Primero viene el identificador del genoma.

> b. Después vienen varias líneas con la secuencia de nuclótidos del genoma completo.



- `coli.gff`: anotación de features en el genoma


El contenido del archivo es:

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM584v2
#!genome-build-accession NCBI_Assembly:GCF_000005845.2
##sequence-region NC_000913.3 1 4641652
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=511145

NC_000913.3     RefSeq  region  1       4641652 .       +       .       ID=NC_000913.3:1.>
NC_000913.3     RefSeq  gene    190     255     .       +       .       ID=gene-b0001;Dbx>
NC_000913.3     RefSeq  CDS     190     255     .       +       0       ID=cds-NP_414542.>
NC_000913.3     RefSeq  gene    337     2799    .       +       .       ID=gene-b0002;Dbx>
NC_000913.3     RefSeq  CDS     337     2799    .       +       0       ID=cds-NP_414543.>

```

Formato: 

> a. Es un formato gff tabular, es decir, cada dato es separado por tabulador.
> 
> b. Cada renglón en el formato gff es una elemento genético anotado en el genoma, que se le denomina `feature`, éstos features pueden ser genes, secuencias de inserción, promotores, sitios de regulación, todo aquello que este codificado en el DNA y ocupe una región en el genoma de  E. coli.

> c. Los atributos de cada columna par cada elemento genético son

>```
1. seqname. Nombre del cromosoma
2. source. Nombre del programa que generó ese elemento
3. feature. Tipo de elemento
4. start. Posición de inicio
5. end. Posición de final
6. score. Un valor de punto flotante
7. strand. La cadena (+ , - )
8. frame. Marco de lectura
9.  attribute. Pares tag-value, separados por coma, que proveen información adicional
```


### Preguntas de investigación 

1. ¿Qué genes involucrados en el desarrollo del tubo neural, glándulas suprarrenales y progresión del neuroblastoma están diferencialmente expresados en las muestras knockout de MOXD1?

Respuesta: Esta pregunta se abordará realizando un análisis de expresión diferencial utilizando los datos crudos de RNA-seq de las muestras knockout y control. Emplearemos herramientas de Python como pyDEseq2 o statsmodels para calcular qué genes muestran diferencias significativas en sus niveles de expresión entre los dos grupos. Luego, visualizaremos los genes diferencialmente expresados mediante un heatmap utilizando la biblioteca seaborn. Esta visualización nos permitirá identificar patrones de expresión entre las muestras knockout y control, facilitando la identificación de genes clave relacionados con el desarrollo del tubo neural, glándulas suprarrenales y la progresión del neuroblastoma.

2. ¿Qué funciones biológicas relacionadas con el metabolismo de iones de cobre y el desarrollo glandular están enriquecidas en los genes sobreexpresados y subexpresados en las muestras knockout de MOXD1?

Respuesta: Una vez identificados los genes diferencialmente expresados, se llevará a cabo un análisis de enriquecimiento funcional para determinar qué funciones biológicas y rutas están sobrerrepresentadas entre los genes afectados. Utilizaremos la biblioteca de Python gseapy para realizar este análisis, enfocándonos en funciones relacionadas con el metabolismo de iones de cobre y el desarrollo glandular. Esta técnica nos permitirá conectar los cambios en la expresión génica con procesos biológicos específicos, proporcionando una mejor comprensión de cómo la disrupción de MOXD1 afecta rutas clave en el desarrollo embrionario.

3. ¿Cómo afecta la alteración de la vía de señalización relacionada con MOXD1 el metabolismo de cobre y la progresión del neuroblastoma en las muestras knockout?

Respuesta: Para responder a esta pregunta, realizaremos un análisis más detallado de las vías de señalización implicadas en la función de MOXD1. Después de identificar los genes de la vía que han sido afectados en el análisis de expresión diferencial, utilizaremos herramientas como pathviewpy o ReactomePy para mapear estas alteraciones en las vías biológicas. Este análisis permitirá visualizar cómo se han desregulado las rutas específicas relacionadas con el metabolismo de cobre y el neuroblastoma en las muestras knockout, ayudando a comprender las implicaciones biológicas y clínicas de la disrupción de MOXD1.

- Nota: las herramientas descritas están sujetas a cambios o nuevas implementaciones.


### Resultados
 

<!-- ### X. Pregunta 

Archivo(s):     

Algoritmo: 

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```






## Análisis y Conclusiones

 <!-- Describir todo lo que descubriste en este análisis -->


## Referencias

1. Fredlund E., Andersson S., Ferreira M., Mohlin S. MOXD1 is a lineage-specific gene and a tumor suppressor in neuroblastoma. Science Advances. 21 de Junio del 2024. DOI: 10.1126/sciadv.ado1583

2. GEO Accession GSE242700: Trunk neural crest gene MOXD1 affects embryonic development. Disponible en: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700
