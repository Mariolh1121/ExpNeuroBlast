import pandas as pd

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
    data.drop(columns = not_exp_data, inplace=True)

    # Applying cut off value 
    data = data.T
    filtered_data = data.loc[:, data.sum(axis=0) > min_count]
    filtered_data.to_csv(output_file)
    return output_file