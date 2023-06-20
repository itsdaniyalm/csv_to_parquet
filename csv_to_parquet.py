from pyarrow import csv, parquet
from datetime import datetime


in_path = input("Enter complete path of csv file along with filename and extension:")
out_path = input("Enter output path:")
out_file = input("Enter parquet file name:")

out_final = out_path+out_file+'.parquet'

table = csv.read_csv(in_path)
parquet.write_table(table, out_final)