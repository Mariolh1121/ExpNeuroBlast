import argparse
from run_deseq2 import run_deseq2
import logging

# Create logger logger
logger = logging.getLogger("ap_rundese2_data")
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
    parser.add_argument("-c", "--control", type=int, help="Number of control samples in the data")
    parser.add_argument("-t", "--treated", type=int, help="Number of treated samples in the data")

    args = parser.parse_args()

    control = ['control'] * args.control
    treated = ['treated'] * args.treated
    conditions = control + treated

    run_deseq2(
        args.input_file,
        args.output_file,
        conditions,
        ('condition', 'treated', 'control')
    )
    logger.info(f"Expression data saved in: {args.output_file}")

if __name__ == "__main__":
    main()