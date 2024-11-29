import pandas as pd
import re
import logging
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Create logger logger
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
# File handler to save logs in a file
file_handler = logging.FileHandler('../logger/utils')
file_handler.setLevel(logging.INFO)
# Console handler to show logs in the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# Log format
formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s')
# Asignar format to the handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def ensemblid_gensymbol(expression_file : str, ensembl_gtf_file: str):
    """
    Return the dataframe of the dds expression with the gensymbol from a gtf ensemble file 

    Args:
        expression_file: csv that contains the processed expression data
        ensembl_gtf_file: ensemble gtf file that contains information of the annotations of an specific organism
    """
    def extract_gene_info(line):
        """
        Search for the ensembl id and gen name in a gtf file
        """
        gene_id_match = re.search(r'gene_id "([^"]+)"', line)  # Extract gene_id
        gene_name_match = re.search(r'gene_name "([^"]+)"', line)  # Extract gene_name
        return (
            gene_id_match.group(1) if gene_id_match else None,
            gene_name_match.group(1) if gene_name_match else None,
        )
    ids_symbol = dict()
    found = 0 
    with open(ensembl_gtf_file, "r") as f:
        logger.info('Processing gtf file')
        for line in f:
            if not line.startswith("#"):
                fields = line.strip().split("\t")
                if len(fields) > 8 and fields[2] == 'gene':
                    gen_id, gene_name = extract_gene_info(fields[8])
                    if not gene_name: 
                        ids_symbol[gen_id] = gen_id
                    else: 
                        ids_symbol[gen_id] = gene_name
                        found += 1
    logger.info(f'A total of {found} gene names were found in gtf file')
    df = pd.read_csv(expression_file, index_col = 0)
    logger.info('Mapping symbols in df')
    df['symbol'] = df.index.map(ids_symbol)
    df.to_csv(expression_file, index = True)
    logger.info('Saving df in csv file')
    return expression_file

def volcano_plot(expression_data: str, output_file: str, pval_treshold: int = 0.05, log2fc_treshold: int = 1):
    """
    Makes a Volcano plot with the expression data file 

    Args:
        expression_file: csv that contains the processed expression data
        pval_tresh: Treshold of the adjusted p value
        log2fc_tresh = Treshold of the log2fold change
    """
    results = pd.read_csv(expression_data, index_col = 0)
    results = results.where(pd.notna(results), None)
    # Filtering the data
    over_expressed = results[(results.padj < pval_treshold) & (abs(results.log2FoldChange) > log2fc_treshold)]
    # Changing None for gen id in symbol field
    for index, row in over_expressed.iterrows():
        if row.symbol == None:
            over_expressed.at[index, 'symbol'] = index
    symbols = list(over_expressed.symbol)
    logger.info(f'{len(symbols)} genes were differentially expressed')
    results["-log10_pval"] = -np.log10(results['padj'])
    results['highlight'] = (abs(results.log2FoldChange) > log2fc_treshold) & (results.padj < pval_treshold)
    sns.scatterplot(data=results,
                x=results['log2FoldChange'], 
                y= results['-log10_pval'],
                hue='highlight',  
                palette={True: 'red', False: 'blue'}, 
                alpha=0.7)
    
    plt.axhline(y=-np.log10(pval_treshold), color='grey', linestyle='--')
    plt.axvline(x = log2fc_treshold, color='grey', linestyle='--')
    plt.axvline(x =- log2fc_treshold, color='grey', linestyle='--')
    plt.xlabel("Log2 Fold Change")
    plt.ylabel("-log10_pval")

    # Adding legend elements
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='ED'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='NED')
    ]
    plt.legend(handles=legend_elements, title="ED genes", loc="upper right")
    plt.show()
    plt.savefig("../../resuslts/volcano_plot.png")
    logger.info(f'The plot image was saved in ../../results/volcano_plot.png')
    logger.info(f'The differentially expressed genes with the parameters were saved in {output_file}')
    results.to_csv(output_file, index = True)
    return output_file
