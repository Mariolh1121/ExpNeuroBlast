import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import logging

# Create logger logger
logger = logging.getLogger("ap_process_data")
logger.setLevel(logging.INFO)
# File handler to save logs in a file
file_handler = logging.FileHandler('../logger/run_deseq2')
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

def run_deseq2(input_file: str,  output_file: str, conditions: list, stat_res_com: tuple):
    """
    Run DESeq2 and save results

    Args:s
        input_file: Path of the input file 
        conditions: List of experimental conditions (control / treated)
        output_file: Path to save the results. 
        contrast: Tuple of what we are comparing in the stats result ('condition', 'treated', 'control')
    """
    # Loading processed file
    data = pd.read_csv(input_file, index_col=0)

    # Creating meta data
    md = pd.DataFrame({'condition': conditions}, index = data.index)

    # Running DEseq2
    dds = DeseqDataSet(counts = data, metadata = md, design_factors = 'condition')
    dds.deseq2()

    # Taking the results
    stat_res = DeseqStats(dds, contrast = stat_res_com)
    stat_res.summary()
    results = stat_res.results_df
    print(results)

    # Returning the output file
    logger.info('Saving df in csv file')
    results.to_csv(output_file, index = True)
    return output_file