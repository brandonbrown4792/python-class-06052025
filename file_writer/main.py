import csv

file_path = "my_file.csv"

data = [
    [1, 'Brandon', 'Computer'],
    [2, 'Luxia', 'Computer']
]

# Generate report
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for entry in data:
        writer.writerow(entry)
    