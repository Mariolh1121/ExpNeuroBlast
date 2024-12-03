# Proyecto Biopython: Análisis de expresión diferencial del gen MOXD1 durante el desarrollo embrionario de Gallus gallus

Proyecto que contiene distintos scripts para realizar un análisis de expresión diferencial para el knock del gen MOXD1 en gallus gallus. 

## Uso

Este proyecto se puede usar tanto para línea de comandos o importando las funciones de los scripts que se encuentran en la carpeta análisis. Dentro de este proyecto se utilizaron las siguientes librerías o dependencias:
+ pandas
+ numpy
+ matplotlib
+ seaborn
+ pydeseq2
+ logging

#### Para correrlo desde línea de comandos:
Dentro de la carpeta scripts que se encuentra en src

ap_process_data.py: Process raw expression data

``` bash
python3 ap_process_data.py 'input_file' 'output_file' -m 10 -o 'sample-gen' -n ''
```

Parámetros:
+ input_file: Path to the expression processed data file
+ output_file: Path to save the processed data
+ min_count(o): Cut-off value of minimun counts by gen -> default: 10
+ orientation(o): The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column) -> default: 'gen-sample'
+ not_exp_data(o): Rows or columns that are not part of the gene expression counts -> default: ''

ap_rundeseq2: Process feature counts file por differential expression analysis with rundeseq2

``` bash
python3 python3 ap_rundeseq2.py 'input_file' 'output_file' -c 9 -t 12 
```
Salida: 
+ Archivo csv con los datos procesados guardados en la carpeta de results

Parámetros:
+ input_file: Path to the expression raw data file
+ output_file: Path to save the processed data
+ control: Number of control samples in the data
+ treated: Number of treated samples in the data

Salida: 
+ Archivo csv del análisis de expresión diferencial guardado en results

``` bash
python3 ap_results_data.py 'input_file' 'gtf_file' 'output_file' -p 0.05 -l 1
```

Parámetros:
+ input_file: Path to the gene expression analysis file
+ output_file: Path to save the expressed genes data by the selected paramteres of the user
+ pvalue(o): Treshold value of the pvalue -> default: 0.05
+ log2FoldChange(o): Treshold value for the log2FoldChange -> default: 0.05

Salida: 
+ Archivo csv con los genes expresados diferencialmente con tus atributos guardados en la carpeta de results
+ Volcano plot del análisis guardado en la carpeta de results

#### Para correrlo desde python:
Dentro de la carpeta analysis que se encuentra en src

```python
from prepare_data import preprocess_data
def preprocess_data(input_file: str, output_file: str, min_count: int = 10 , orientation: str = 'gen-sample', not_exp_data: list = [])
    """
    Filtrates genes with low expression in the count data and eliminates genes with no 
    expression in any condition 

    Args:
        input_file: Path to the expression raw data file
        output_file: Path to save the processed data
        min_count: Cut-off value of minimun counts by gend
        orientation: The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column)
        not_exp_data: Rows or columns that are not part of the gene expression counts
    """
```
Salida:
+ Archivo csv del análisis de expresión diferencial guardado en results

```python
from run_deseq2 import run_deseq2
def run_deseq2(input_file: str,  output_file: str, conditions: list, stat_res_com: tuple):
    """
    Run DESeq2 and save results

    Args:s
        input_file: Path of the input file 
        conditions: List of experimental conditions (control / treated)
        output_file: Path to save the results. 
        contrast: Tuple of what we are comparing in the stats result ('condition', 'treated', 'control')
    """
```
Salida:
+ Archivo csv del análisis de expresión diferencial guardado en results

```python
from utils import ensemblid_gensymbol
def ensemblid_gensymbol(expression_file : str, ensembl_gtf_file: str):
    """
    Return the dataframe of the dds expression with the gensymbol from a gtf ensemble file 

    Args:
        expression_file: csv that contains the processed expression data
        ensembl_gtf_file: ensemble gtf file that contains information of the annotations of an specific organism
    """
```
Salida: 
+ Archivo csv del análisis de expresión diferencial con la columna añadida de symbol que contiene el nombre de los genes encontrados en el archivo gtf

```python
from utils import volcano_plot
def volcano_plot(expression_data: str, output_file: str, pval_treshold: int = 0.05, log2fc_treshold: int = 1):
    """
    Makes a Volcano plot with the expression data file 

    Args:
        expression_file: csv that contains the processed expression data
        pval_tresh: Treshold of the adjusted p value
        log2fc_tresh = Treshold of the log2fold change
    """
    """
```
Salida: 
+ Archivo csv con los genes expresados diferencialmente con tus atributos guardados en la carpeta de results
+ Volcano plot del análisis guardado en la carpeta de results

## Datos

Los scripts funcionan para recibir datos de un archivo feature counts, donde esta diseñado para operar con datos del knock out de MOXD1 para gallus gallus extraídos de la base de datos de GEO con el siguiente accesion [GSE242700](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700) .

## Metadatos y documentación

Este README ofrece información de uso básico de los scripts tanto para correr las funciones directamente desde python o desde la línea de comandos. Los datos que utilizamos estan disponibles en [GSE242700](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242700) .

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: Mariolh. (2024). GitHub - Mariolh1121/ExpNeuroBlast: To do. . . GitHub. https://github.com/Mariolh1121/ExpNeuroBlast/tree/main.

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: 
[Silvana Yalú Cristo Martínez (silvanac@lcg.unam.mx) o [Mario Alberto Limón Hernández (mariolh@lcg.unam.mx)]  
