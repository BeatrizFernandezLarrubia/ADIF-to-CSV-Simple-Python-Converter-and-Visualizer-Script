# This simple script converts ADI/ADIF (Amateur Data Interchange Format) files to CSV (Comma-Separated Values) format, in order to facilitate easier data analysis and manipulation.
# Author: Beatriz Fernández Larrubia (DJ0DE)
# Date: 3rd January 2026
# Requirements: pandas library, python 3.x
# Usage: python adif_to_csv.py <input_adif_file> <output_csv_file>
# Copyright: This script is provided "as is" without any warranty. Use at your own risk. Distributed under the GPL License.

import pandas as pd
import re
import os
import argparse
import time

def parse_adif(adif_content):
    records = []
    current_record = {}
    adif_content = adif_content.replace('\n', ' ').replace('\r', ' ')
    entries = re.split(r'<eor>', adif_content, flags=re.IGNORECASE)

    for entry in entries:
        if not entry.strip():
            continue
        fields = re.findall(r'<(.*?)>([^<]*)', entry)
        for field, value in fields:
            field_name = field.split(':')[0].strip().upper()
            current_record[field_name] = value.strip()
        if current_record:
            records.append(current_record)
            current_record = {}
    
    return records

def adif_to_csv(adif_file, csv_file):
    with open(adif_file, 'r', encoding='utf-8', errors='ignore') as f:
        adif_content = f.read()
    
    records = parse_adif(adif_content)
    df = pd.DataFrame(records)
    df.to_csv(csv_file, index=False)
    print(f"Converted {adif_file} to {csv_file}")
    print(f'Note: This simple conversion script may not handle all ADIF fields perfectly, for example if the band field has differing formatting (40M vs 40m). Please verify the output CSV file or visualization for accuracy, and change the .adi file if necessary before running the script again.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert ADIF files to CSV format.')
    
    # First option: command line arguments
    parser.add_argument('adif_file', help='Path to the input ADIF file', nargs='?')
    parser.add_argument('csv_file', help='Path to the output CSV file', nargs='?')
    args = parser.parse_args()
    
    # Second option: hardcoded file paths. 
    adif_file_path = 'file.adi'  # CHANGE THIS TO YOUR OWN PATH FILE.
    time_aux = time.strftime("%Y%m%d-%H%M%S")
    csv_file_path = f"converted_csv_file_{time_aux}.csv" # CHANGE THIS TO YOUR OWN PATH FILE IF WANTED.

    adif_file = args.adif_file if args.adif_file else adif_file_path
    csv_file = args.csv_file if args.csv_file else csv_file_path
    print(f"Input ADIF file: {adif_file}")
    print(f"Output CSV file: {csv_file}")

    # Check if the ADIF file exists
    if not os.path.isfile(adif_file):
        print(f"Error: The provided file path {adif_file} does not exist.")
        exit(1)

    # Warn if the CSV file does not exist (it will be created)
    if not os.path.isfile(csv_file):
        print(f"Warning: The file {csv_file} does not exist and will be created.")
    if os.path.abspath(adif_file) == os.path.abspath(csv_file):
        print("Error: The input ADIF file and output CSV file paths cannot be the same.")
        exit(1)
    if not csv_file.lower().endswith('.csv'): # Check that the csv file is actually a .csv file
        print("Error: The output file must have a .csv extension.")
        exit(1)
    if not adif_file.lower().endswith('.adi') and not adif_file.lower().endswith('.adif'): # Check that the adif file is actually a .adi or .adif file
        print("Error: The input file must have a .adi or .adif extension.")
        exit(1)
    
    adif_to_csv(adif_file, csv_file)