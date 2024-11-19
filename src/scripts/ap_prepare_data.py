import argparse
from prepare_data import preprocess_data

def main():
    parser = argparse.ArgumentParser(description="Processing raw expression data")
    parser.add_argument("input_file", help="Path to the expression raw data file")
    parser.add_argument("output_file", help="Path to save the processed data")
    parser.add_argument("--min_count", type=int, default=10, help="Cut-off value of minimun counts by gen")
    parser.add_argument("--orientation",type=str, default='gen-sample', help="The orientation of the Feature Counts file, could be gene-sample or sample-gen (row-column)")
    parser.add_argument("--not_exp_data",type=list, default= [], help="Rows or columns that are not part of the gene expression counts")

    args = parser.parse_args()

    preprocess_data(args.input_file, args.output_file, min_count = args.min_count, orientation = args.orientation, not_exp_data= args.not_exp_data)
    print(f"Processed data saved in : {args.output_file}")

if __name__ == "__main__":
    main()