import os
import csv
from datetime import datetime

def main(filename) :
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".csv")

    with open(base + ".csv") as f: 
        reader = csv.reader(f)  # create a CSV reader
        for row in reader:  # skip the lines until we encounter the second CSV structure/header
            if row and row[3] != "200" and row[3] != "responseCode":
                print("*********************************")
                print("Label: " + row[2])
                print("Response Code: " + row[3])
                print("Response Message: " + row[4])
                print("Failure Message: " + row[8])
                timestamp = int(row[0][:10])
                dt_object = datetime.fromtimestamp(timestamp)
                print("Time: " + str(dt_object) + " PST")

if __name__ == "__main__":
    main('Jmeter_log1.jtl')