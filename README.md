# CSV to JSON Converter

Converts CSV files to JSON arrays. Each row becomes an object with column headers as keys.

## Usage

```bash
python csv_to_json.py input.csv
python csv_to_json.py input.csv -o output.json
python csv_to_json.py input.csv --indent 4
```

If no output file is specified, it uses the CSV filename with `.json` extension.

## Behavior

- Empty cells → `null`
- Numeric strings → integers or floats (auto-detected)
- Column headers → JSON keys
- Default indent: 2 spaces

## Example

Input CSV:
```csv
spkid,full_name,pdes,neo,pha,H,G
20000433,433 Eros (A898 PA),433,Y,N,10.38,0.46
20000719,719 Albert (A911 TB),719,Y,N,15.59,
```

Output JSON:
```json
[
  {
    "spkid": 20000433,
    "full_name": "433 Eros (A898 PA)",
    "pdes": 433,
    "neo": "Y",
    "pha": "N",
    "H": 10.38,
    "G": 0.46
  },
  {
    "spkid": 20000719,
    "full_name": "719 Albert (A911 TB)",
    "pdes": 719,
    "neo": "Y",
    "pha": "N",
    "H": 15.59,
    "G": null
  }
]
```