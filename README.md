# ADIF to CSV Simple Python Converter and Visualizer Script
These two simple scripts have as goals to give a very quick and easy conversion from a .adi or .adif file (Amateur Data Interchange Format) to a CSV file for easy loading into Excel or to do further data analysis with Pandas or other libraries, and to provide a quick visualization for the converted CSV file. They were developed with the use case of visualizing Amateur Radio logs easily after downloading them from QRZ.com, Wavelog, or others.

The logic has been divided into two different scripts for ease of use. adif_to_csv.py contains the conversion logic, and visualize_converted_csv.py contains the easy visualization logic.

Some details:
- Both scripts are independent of each other. They have been lightly tested, mostly the parsing of the input/output arguments.
- Libraries used are pandas and ydata_profiling.
- Python version used to develop was 3.11.9.
- Last Revision: both scripts Jan 3rd 2026
