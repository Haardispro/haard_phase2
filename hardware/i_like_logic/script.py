import csv

# Replace with your CSV file name
filename = "data.csv"

# Empty string to store all data from the last column
result = ""

with open(filename, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # make sure row is not empty
            result += row[-1] + " "  # take the last column and add space between entries

print(result.strip())  # print the combined string

