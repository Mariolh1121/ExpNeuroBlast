import argparse
from utils import ensemblid_gensymbol, volcano_plot
import logging

# Create logger logger
logger = logging.getLogger("ap_process_data")
logger.setLevel(logging.INFO)
# File handler to save logs in a file
file_handler = logging.FileHandler('../logger/ap_results_data')
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
    parser.add_argument("input_file", help="Path to the expression processed data file")
    parser.add_argument("output_file", help="Path to the expression genes data file")
    parser.add_argument("ensembl_gtf_file", help="Path to the gtf ensemble annotated genes file")
    parser.add_argument("-p", "--pvalue", type=float, default = 0.05, help="Treshold value of the pvalue")
    parser.add_argument("-l", "--log2FoldChange", type=float, default = 1, help="The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column)")
    args = parser.parse_args() 

    ensemblid_gensymbol(
        args.input_file,
        args.ensembl_gtf_file
    )
    logger.info(f"Processed data saved in: {args.input_file}")

    volcano_plot(
        args.input_file,
        args.output_file,
        args.pvalue,
        args.log2FoldChange
    )

if __name__ == "__main__":
    main()