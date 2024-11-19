import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

def run_deseq2(input_file: str, conditions: list, output_file: str, stat_res_con: tuple):
    """
    Run DESeq2 and save results

    Args:
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
    stat_res = DeseqStats(dds, contrast = stat_res_con)
    stat_res.summary()
    results = stat_res.results_df
    print(results)

    # Returning the output file
    results.to_csv(output_file)
    return output_file