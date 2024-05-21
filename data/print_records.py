import json
import argparse

# Function to read and print records from the JSONL file
def read_and_print_records(file_path, num_records=10):
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if i >= num_records:
                break
            record = json.loads(line)
            print(json.dumps(record, indent=4))  # Pretty-print the JSON record

if __name__ == "__main__":
    # Setting up command-line argument parsing
    parser = argparse.ArgumentParser(description="Read and print records from a JSONL file.")
    parser.add_argument('file_path', type=str, help="Path to the JSONL file")
    parser.add_argument('--num_records', type=int, default=5, help="Number of records to print (default: 5)")

    args = parser.parse_args()

    # Reading and printing the specified number of records from the file
    read_and_print_records(args.file_path, num_records=args.num_records)


    # usage

    # python print_records.py Appliances.jsonl --num_records 5
    # python print_records.py all_appliances.jsonl --num_records 1
