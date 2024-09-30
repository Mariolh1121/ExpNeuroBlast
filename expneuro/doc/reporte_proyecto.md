# Análisis de expresión del gen MOX_1

Nombre: Mario Alberto Limón Hernández mariolh@lcg.unam.mx
Nombre: Silvana Yalu Cristo Martinez silavanac@lcg.unam.mx

Fecha:  10/09/2024


## Introducción

Este proyecto tiene como objetivo analizar la función del gen *MOXD1* durante el desarrollo de la cresta neural en Gallus gallus. A través de un análisis de expresión génica diferencial entre embriones knockout de MOXD1 y controles, se busca identificar los genes y rutas de señalización involucrados en el desarrollo normal y cómo estos se ven afectados en ausencia de MOXD1.

El gen MOXD1 ha sido previamente identificado como un potencial supresor tumoral en neuroblastoma, un cáncer infantil derivado de las células de la cresta neural. Por lo tanto, este estudio podría proporcionar nueva información sobre el desarrollo normal de la cresta neural y su relación con procesos patológicos como el cáncer.

## Planteamiento del problema

La falta de información sobre los mecanismos moleculares que dependen del gen MOXD1 durante el desarrollo embrionario plantea una brecha importante en la comprensión de la biología de la cresta neural. MOXD1 ha sido vinculado a funciones importantes en el desarrollo de las glándulas suprarrenales y en la prevención del neuroblastoma, pero su rol exacto en los primeros eventos de desarrollo embrionario sigue siendo desconocido.

Este proyecto busca investigar cómo la ausencia de MOXD1 afecta el desarrollo de la cresta neural y qué genes y rutas de señalización se ven alterados, con el fin de mejorar nuestra comprensión de su papel biológico y de las posibles implicaciones patológicas cuando está ausente.


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
- GSE242700_2020_75_R2_gene_id.featureCounts.tsv: Formato tsv
Program:featureCounts v2.0.1; Command:"/opt/conda/envs/rnatools/bin/featureCounts" "-T" "20" "-t" "exon" "-a" "/projects/fs1/medpvb/genomicData/gallus/Gallus_gallus.GRCg6a.101.gtf" "-g" "gene_id" "-o" "/projects/fs1/medpvb/proj/bulkRNA/201013_MV/048_TruSeq/CTG_output/2020_75_R2/Quantification/../Quantification/2020_75_R2_gene_id.featureCounts.txt" "-p" "-s" "2" "CTRL_10" "CTRL_12" "CTRL_1" "CTRL_2" "CTRL_3" "CTRL_4" "CTRL_5" "CTRL_6" "CTRL_8" "MOX_10" "MOX_12" "MOX_13" "MOX_14" "MOX_1" "MOX_2" "MOX_3" "MOX_5" "MOX_6" "MOX_7" "MOX_8" "MOX_9" 
El contenido del archivo viene en la siguiente tabla:
| Columna    | Significado                                                                                 |
|------------|---------------------------------------------------------------------------------------------|
| Geneid     | Identificador único del gen en el análisis                                                   |
| Chr        | Cromosoma en el que se encuentra el gen                                                      |
| Start      | Posición inicial del gen en el cromosoma                                                     |
| End        | Posición final del gen en el cromosoma                                                       |
| Strand     | Cadena (sentido o antisentido) del ADN en la que se transcribe el gen                        |
| Length     | Longitud total del gen (en pares de bases)                                                   |
| CTRL_10    | Conteos de expresión para la condición control en la réplica 10                              |
| CTRL_12    | Conteos de expresión para la condición control en la réplica 12                              |
| CTRL_1     | Conteos de expresión para la condición control en la réplica 1                               |
| CTRL_2     | Conteos de expresión para la condición control en la réplica 2                               |
| CTRL_3     | Conteos de expresión para la condición control en la réplica 3                               |
| CTRL_4     | Conteos de expresión para la condición control en la réplica 4                               |
| CTRL_5     | Conteos de expresión para la condición control en la réplica 5                               |
| CTRL_6     | Conteos de expresión para la condición control en la réplica 6                               |
| CTRL_8     | Conteos de expresión para la condición control en la réplica 8                               |
| MOX_10     | Conteos de expresión para la condición experimental (MOX) en la réplica 10                   |
| MOX_12     | Conteos de expresión para la condición experimental (MOX) en la réplica 12                   |
| MOX_13     | Conteos de expresión para la condición experimental (MOX) en la réplica 13                   |
| MOX_14     | Conteos de expresión para la condición experimental (MOX) en la réplica 14                   |
| MOX_1      | Conteos de expresión para la condición experimental (MOX) en la réplica 1                    |
| MOX_2      | Conteos de expresión para la condición experimental (MOX) en la réplica 2                    |
| MOX_3      | Conteos de expresión para la condición experimental (MOX) en la réplica 3                    |
| MOX_5      | Conteos de expresión para la condición experimental (MOX) en la réplica 5                    |
| MOX_6      | Conteos de expresión para la condición experimental (MOX) en la réplica 6                    |
| MOX_7      | Conteos de expresión para la condición experimental (MOX) en la réplica 7                    |
| MOX_8      | Conteos de expresión para la condición experimental (MOX) en la réplica 8                    |
| MOX_9      | Conteos de expresión para la condición experimental (MOX) en la réplica 9                    |

- GSE242700_family.soft: Formato SOFT:
Contiene información sobre el experimento de expresión génica en el que se estudió el gen MOXD1 y su influencia en el desarrollo embrionario de células de la cresta neural del tronco en embriones de pollo, que contiene la siguiente información:
+ Título: El gen de la cresta neural del tronco MOXD1 afecta el desarrollo embrionario.
+ Accesión GEO: GSE24270
+ Estado: Público desde el 13 de septiembre de 2023.
+ Objetivo: Evaluar el impacto del gen MOXD1 en el desarrollo embrionario temprano, mediante su eliminación en células de la cresta neural del tronco usando el enfoque CRISPR/Cas9 en embriones de pollo
+ Diseño experimental
+ Plataforma utilizada: GPL26853

<!-- 



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
NC_0009
```


#### Preguntas de investigación
> ¿Pregunta X?
Respuesta: Describir el trabajo que implica o pasos a seguir para resolver esta pregunta.



-->


## Resultados
 

<!-- ### X. Pregunta 

Archivo(s):     

Algoritmo: 

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```

-->




## Análisis y Conclusiones

 <!-- Describir todo lo que descubriste en este análisis -->


## Referencias
<!-- Registrar todas las referencias consultadas. Se sugiere formato APA. Ejemplo:
 
 [1] Frederick R. Blattner et al., The Complete Genome Sequence of <i>Escherichia coli</i> K-12.Science277,1453-1462(1997).DOI:10.1126/science.277.5331.1453
 
 -->
