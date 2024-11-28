import argparse
from prepare_data import preprocess_data
import logging

# Create logger logger
logger = logging.getLogger("ap_process_data")
logger.setLevel(logging.INFO)
# File handler to save logs in a file
file_handler = logging.FileHandler('../logger/ap_process_data')
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

def main():
    parser = argparse.ArgumentParser(description="Processing raw expression data")
    parser.add_argument("input_file", help="Path to the expression raw data file")
    parser.add_argument("output_file", help="Path to save the processed data")
    parser.add_argument("-m", "--min_count", type=int, default=10, help="Cut-off value of minimum counts by gene")
    parser.add_argument("-o", "--orientation", type=str, default='gen-sample', help="The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column)")
    parser.add_argument("-n", "--not_exp_data", nargs='+', type=str, default='', help="Rows or columns that are not part of the gene expression counts")

    args = parser.parse_args() 

    preprocess_data(
        args.input_file,
        args.output_file,
        min_count=args.min_count,
        orientation=args.orientation,
        not_exp_data=args.not_exp_data
    )
    logger.info(f"Processed data saved in: {args.output_file}")

if __name__ == "__main__":
    main()