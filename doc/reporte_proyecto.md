# Análisis de expresión del gen MOX_1
# Análisis de expresión diferencial del gen MOXD1 durante el desarrollo embrionario de Gallus gallus 

Nombre: Mario Alberto Limón Hernández mariolh@lcg.unam.mx
Nombre: Silvana Yalu Cristo Martinez silavanac@lcg.unam.mx

Fecha:  10/09/2024

## Introducción

El neuroblastoma es uno de los tipos de cáncer más comunes en la infancia, derivado de células de la cresta neural, una población celular que da origen a diversos tipos de tejidos durante el desarrollo embrionario temprano. Estas células son extremadamente plásticas y pueden diferenciarse en neuronas, células gliales, melanocitos y células de la médula adrenal, entre otras. La disregulación genética en esta población celular es un factor clave en la oncogénesis del neuroblastoma.

Un gen que ha mostrado estar fuertemente relacionado con la progresión del neuroblastoma es MOXD1. Este gen, asociado al metabolismo de iones de cobre y al desarrollo de las glándulas suprarrenales, ha sido recientemente identificado como un posible supresor tumoral en neuroblastoma, sin embargo, su papel en el desarrollo embrionario en general y su implicación en el establecimiento de rutas de señalización cruciales, como las involucradas en la diferenciación neural y la homeostasis de metales, sigue siendo poco conocido.

Recientes estudios, como el trabajo de Fredlund et al. (2023) publicado en Science Advances, han investigado el papel de MOXD1 utilizando múltiples organismos modelo, incluidos ratones y pollos (Gallus gallus). En su investigación, los autores demostraron que la disrupción de MOXD1 provoca un desarrollo embrionario anormal, lo cual refuerza su papel regulador en procesos cruciales como el desarrollo de la glándula adrenal y en la progresión de tumores neuroblásticos. Estos hallazgos sugieren que MOXD1 tiene una función crítica en mantener el equilibrio adecuado de la señalización celular durante la diferenciación.

Este proyecto se centrará en investigar cómo la eliminación de MOXD1 mediante un enfoque de knockout en Gallus gallus afecta la expresión génica a nivel global. Para ello, se llevará a cabo un análisis de expresión diferencial utilizando datos de RNA-seq, lo que permitirá identificar genes que cambian su nivel de expresión en respuesta a la pérdida de MOXD1. 

## Planteamiento del problema

El neuroblastoma es un cáncer infantil derivado de células de la cresta neural que sigue siendo una de las principales causas de muerte por cáncer en la infancia. A pesar de los avances en el tratamiento, los mecanismos moleculares que regulan la progresión de este cáncer y su relación con el desarrollo embrionario normal aún no se comprenden completamente. MOXD1 ha sido identificado como un gen supresor tumoral en el neuroblastoma, pero su papel exacto en el desarrollo embrionario, especialmente en procesos clave como el metabolismo de iones de cobre y la diferenciación de tejidos derivados de la cresta neural, sigue sin estar claro.

El knockout de MOXD1 en Gallus gallus ofrece una oportunidad única para investigar cómo su eliminación afecta el desarrollo, así como su conexión con vías biológicas críticas. La falta de comprensión sobre estas vías específicas es un obstáculo para el desarrollo de terapias dirigidas más efectivas contra el neuroblastoma y otras enfermedades relacionadas. Este proyecto busca abordar esta brecha, explorando los efectos de la disrupción de MOXD1 en la expresión génica.
 
## Metodología

Los datos fueron descargados de GEO en NCBI del siguiente link: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700
Los archivos se encuentran en la carpeta data:

``` bash
| -- data
|   | -- GSE242700_2020_75_R2_gene_id.featureCounts.tsv
|   | -- GSE242700_family.soft
```

[Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.]


### A. Servidor y software

> Servidor: NA 

> Usuario: NA

> Software: Python

### B. Datos de Entrada 


#### Metadatos de la carpeta de datos

GEO access: GSE242700
Fecha de descarga: 17/09/2024

| Archivo                                           | Descripción                                         | Tipo |
|:--      |:--           |:--  |
|  GSE242700_2020_75_R2_gene_id.featureCounts.tsv   | Archivo de los datos de expresión con el knockout del gen *MOXD1* | tsv | 
|  GSE242700_family.soft   | Archivo con la información del experimento, y sus adheciones de cada condición | soft |

#### Formato de los archivos

- GSE242700_2020_75_R2_gene_id.featureCounts.tsv: Formato tsv

Program:featureCounts v2.0.1; Command:"/opt/conda/envs/rnatools/bin/featureCounts" "-T" "20" "-t" "exon" "-a" "/projects/fs1/medpvb/genomicData/gallus/Gallus_gallus.GRCg6a.101.gtf" "-g" "gene_id" "-o" "/projects/fs1/medpvb/proj/bulkRNA/201013_MV/048_TruSeq/CTG_output/2020_75_R2/Quantification/../Quantification/2020_75_R2_gene_id.featureCounts.txt" "-p" "-s" "2" "CTRL_10" "CTRL_12" "CTRL_1" "CTRL_2" "CTRL_3" "CTRL_4" "CTRL_5" "CTRL_6" "CTRL_8" "MOX_10" "MOX_12" "MOX_13" "MOX_14" "MOX_1" "MOX_2" "MOX_3" "MOX_5" "MOX_6" "MOX_7" "MOX_8" "MOX_9":

| Columna | Significado |
|---------|-------------|
| Geneid  | Identificador único del gen en el análisis |
| Chr     | Cromosoma en el que se encuentra el gen |
| Start   | Posición inicial del gen en el cromosoma |
| End     | Posición final del gen en el cromosoma |
| Strand  | Cadena del ADN (sentido o antisentido) en la que se transcribe el gen |
| Length  | Longitud total del gen (en pares de bases) |
| CTRL_*  | Conteos de expresión para las condiciones control en las réplicas |
| MOX_*   | Conteos de expresión para las condiciones experimentales en las réplicas |


- GSE242700_family.soft: Formato SOFT:
Contiene información sobre el experimento de expresión génica en el que se estudió el gen MOXD1 y su influencia en el desarrollo embrionario de células de la cresta neural del tronco en embriones de pollo, que contiene la siguiente información:
  + Título: El gen de la cresta neural del tronco MOXD1 afecta el desarrollo embrionario.
  + Accesión GEO: GSE24270
  + Estado: Público desde el 13 de septiembre de 2023.
  + Objetivo: Evaluar el impacto del gen MOXD1 en el desarrollo embrionario temprano, mediante su eliminación en células de la cresta neural del tronco usando el enfoque CRISPR/Cas9 en embriones de pollo
  + Diseño experimental
  + Plataforma utilizada: GPL26853

### Preguntas de investigación 

1. ¿Existe un cambio de expresión entre los genes con el knock de MOXD1?

Respuesta: Esta pregunta se abordará realizando un análisis de expresión diferencial utilizando los datos crudos de RNA-seq de las muestras knockout y control. Emplearemos herramientas de Python como pyDEseq2 o statsmodels para calcular qué genes muestran diferencias significativas en sus niveles de expresión entre los dos grupos.

2. ¿Qué genes estan sobre expresados y sub expresados dada esta condición?

Respuesta: Una vez realizando el análisis de los genes diferencialmente expresados, dado un p-value escogido y un log-fold-change value se filtraran los datos para ver la expresión de estos datos.

3. ¿A qué estan relacionados estos genes diferncialmente expresados?

Respuesta: Despúes de haber extraídos los genes expresialmente diferneciados, se buscarán la relación o implicación de la expresión de estos genes. 

- Nota: las herramientas descritas están sujetas a cambios o nuevas implementaciones.

### Resultados

1. ¿Existe un cambio de expresión entre los genes con el knock de MOXD1?

Algoritmo:
1. Análisar los datos
2. Limpiarlos para realizar el análisis de expresión diferencial
3. Realizar el análisis de expresión diferencial

Solución:

```python
# Importamos las librerías necesarias
import pandas as pd
from prepare_data import preprocess_data
from run_deseq2 import run_deseq2

# Con preprocess_data limpiamos el archivo feature 
preprocess_data('../../data/GSE242700_2020_75_R2_gene_id.featureCounts.tsv',
                 '../../results/preprocessed.csv', min_count=1, 
                 orientation='sample-gen', 
                 not_exp_data=['Start', 'End', 'Strand', 'Length', 'Chr'])

# Realizamos el análisis de expresión diferencial
conditions = ['control', 'control', 'control', 'control', 'control', 'control', 'control', 'control', 'control', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated', 'treated']

comparation = ('condition', 'treated', 'control')

run_deseq2(input_file='../../results/preprocessed_data.csv', 
          output_file= '../../results/expression_analysis.csv', 
          conditions = conditions, 
          stat_res_com =  comparation)
```

2. ¿Qué genes estan sobre expresados y sub expresados dada esta condición?

Algoritmo:

1. Buscar los símbolos o nombres de los genes a partir de su id de Ensembl y añadirlos a los datos originales
2. Dado un p value y un logfold change que en en este casos era establecido a 0.2 y a 1 respectivamente, ver que genes extan expresialmente diferenciado
3. Visualizar volcano plot

Solución:

```python
# Importamos librerías y scripts necesarios
from utils import ensemblid_gensymbol, volcano_plot

# Buscamos el nombre de los genes expresados y no expresados
ensemblid_gensymbol('../../results/expression_analysis.csv', 
                    '../../data/Gallus_gallus_gca000002315v5.GRCg6a.113.gtf')

# Vemos que genes estan diferencialmente expresados con un p-value y un log-fold change
volcano_plot('../../results/expression_analysis.csv', 
             '../../results/df_genes.csv', 
             pval_treshold = 0.2,
             log2fc_treshold = 1)
```

3. ¿A qué estan relacionados estos genes diferncialmente expresados?

Algoritmo:
1. Visualizar el df de los genes expresados
2. Ver si gene name y explorar a que esta relacionado 

Solución:

```python
# Importamos el df de los dato
de_genes = pd.read_csv('../../results/de_genes.csv', index_col = 0)
# Exploramos el contenido del df
de_genes
```
Por lo que podmeos ver no existieron genes sobre expresados, sino subexpresados diferencialmente, por lo que ahora veremos de quienes se tratan.
```python
de_genes.symbol
```
+ C1S -> 	calcium ion binding/serine-type endopeptidase activity
+ DDO -> D-Aspartate Oxidase
+ GC -> Funcioón extra celular desconcodia
+ ENSGALG00000002957 -> Solute carrier family 12 member 3 (Thiazide-sensitive sodium-chloride cotransporter) (Na-Cl symporter)
+ ENSGALG00000048440 -> NA
+ VDR -> Vitamin D3 receptor

## Análisis y Conclusiones

MOXD1 está implicado en la regulación de procesos oxidativos y puede influir en la migración y diferenciación de células de la cresta neural, que son esenciales tanto en el desarrollo embrionario como en la progresión tumoral. El knock-out de MOXD1 podría desregular vías metabólicas críticas, resultando en la subexpresión de estos genes. Estos cambios pueden alterar el microambiente tumoral o la plasticidad celular, impactando la capacidad de las células para proliferar o diferenciarse.

## Referencias

1. Fredlund E., Andersson S., Ferreira M., Mohlin S. MOXD1 is a lineage-specific gene and a tumor suppressor in neuroblastoma. Science Advances. 21 de Junio del 2024. DOI: 10.1126/sciadv.ado1583

2. GEO Accession GSE242700: Trunk neural crest gene MOXD1 affects embryonic development. Disponible en: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700
