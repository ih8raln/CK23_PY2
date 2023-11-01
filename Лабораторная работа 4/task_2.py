# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(csv_file_path,json_file_path) -> None:
    # TODO считать содержимое csv файла
    data = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")