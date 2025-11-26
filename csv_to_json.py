import csv
import json
import argparse
from pathlib import Path


def csv_to_json(csv_file_path, json_file_path=None, indent=2):
    """
    convert a CSV file to JSON format
    input:
        csv_file_path (str)
        json_file_path (str):
        indent (int)
    
    output:
        list: list of dictionaries
    """
    csv_path = Path(csv_file_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"not found: {csv_file_path}")
    
    if json_file_path is None:
        json_file_path = csv_path.with_suffix('.json')
    else:
        json_file_path = Path(json_file_path)
    
    data = []
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cleaned_row = {}
            for key, value in row.items():
                clean_key = key.strip()
                clean_value = value.strip() if value else None
                if clean_value is not None and clean_value != '':
                    try:
                        if '.' in clean_value:
                            clean_value = float(clean_value)
                        else:
                            clean_value = int(clean_value)
                    except ValueError:
                        pass
                else:
                    clean_value = None
                
                cleaned_row[clean_key] = clean_value
            data.append(cleaned_row)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=indent, ensure_ascii=False)
    print(f"success: {csv_path.name} to {json_file_path.name}")    
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    parser.add_argument('-o', '--output', dest='json_file')
    parser.add_argument('--indent', type=int, default=2)
    args = parser.parse_args()
    csv_to_json(args.csv_file, args.json_file, args.indent)

if __name__ == '__main__':
    main()

