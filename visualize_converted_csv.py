# This simple script visualizes data from a converted CSV file with the other script 'adif_to_csv.py' via a profiling report.
# Author: Beatriz Fernández Larrubia (DJ0DE)
# Date: 3rd January 2026
# Requirements: pandas library, ydata-profiling library, python 3.x
# Usage: python visualize_converted_csv.py <input_csv_file>
# Copyright: This script is provided "as is" without any warranty. Use at your own risk. Distributed under the GPL License.

import pandas as pd
import argparse
import os
import sys
import time
from ydata_profiling import ProfileReport

def load_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

def visualize_data(df):
    print("Visualizing data...")

    profile = ProfileReport(df, title="ADIF to CSV Data Profile", explorative=True)
    time_aux = time.strftime("%Y%m%d_%H%M%S")
    output_file = f"data_profile_report_{time_aux}.html"
    profile.to_file(output_file)
    print(f"Profile report saved to {output_file}. Open this file in a web browser to view the report.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize data from a converted CSV file.')

    # First option: command line arguments
    parser.add_argument('csv_file', help='Path to the input CSV file', nargs='?')
    args = parser.parse_args()
    
    # Second option: hardcoded file path.
    csv_file_path = 'converted_csv_file.csv'  # CHANGE THIS TO YOUR OWN PATH FILE.

    csv_file = args.csv_file if args.csv_file else csv_file_path

    if not os.path.isfile(csv_file):
        print(f"Error: The provided file path {csv_file} does not exist, exiting.")
        sys.exit(1)
    if not csv_file.lower().endswith('.csv'): # Check that the csv file is actually a .csv file
        print("Error: The input file must have a .csv extension.")
        exit(1)

    data_frame = load_csv(csv_file)

    visualize_data(data_frame)