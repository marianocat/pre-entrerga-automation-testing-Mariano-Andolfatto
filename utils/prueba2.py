import csv
import os

def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    :param file_path: Path to the CSV file.
    :return: List of dictionaries representing the rows in the CSV file.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

ruta = os.path.join(os.path.dirname(__file__), 'datos.csv')  # Adjust the path as needed
print(read_csv(ruta))  # Example usage, replace 'datos.csv' with your actual file path