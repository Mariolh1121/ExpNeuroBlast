import pandas as pd
import logging

# Create logger logger
logger = logging.getLogger("prepare_data")
logger.setLevel(logging.INFO)
# File handler to save logs in a file
file_handler = logging.FileHandler('../logger/prepare_data')
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

def preprocess_data(input_file: str, output_file: str, min_count: int = 10 , orientation: str = 'gen-sample', not_exp_data: list = []):
    """
    Filtrates genes with low expression in the count data and eliminates genes with no 
    expression in any condition 

    Args:
        input_file: Path to the expression raw data file
        output_file: Path to save the processed data
        min_count: Cut-off value of minimun counts by gen
        orientation: The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column)
        delimeter: Delimeter of the file
        not_exp_data: Rows or columns that are not part of the gene expression counts

    """
    # Preparing Data frame 
    data = pd.read_csv(input_file, index_col=0, comment='#', delimiter = '\t')
    if orientation == 'gen-sample':
        data = data.T
    
    # Eliminating not data counts
    try: 
        data.drop(columns = not_exp_data, inplace=True)
        logger.info(f"Columns {not_exp_data} were dropped out")
    except: 
        logger.info("No drop columns from DF")

    # Applying cut off value 
    data = data.T
    filtered_data = data.loc[:, data.sum(axis=0) > min_count]
    filtered_data.to_csv(output_file)
    return output_file
