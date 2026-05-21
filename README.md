<samp>

# CSV to JSON Converter

<p>
CSV to JSON Converter is a small Python CLI that transforms CSV rows into JSON objects keyed by column headers. It includes sample data, automatic type conversion, indentation control, and predictable output naming.
</p>

<p>
Built with <strong>Python, argparse, csv/json standard libraries, and sample asteroid data</strong>.
</p>

<p>
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
</p>

## Highlights

<ul>
  <li>Converts empty cells to <code>null</code> and numeric strings to numbers where possible.</li>
  <li>Supports explicit output paths and configurable JSON indentation.</li>
  <li>Uses only Python standard-library modules for a lightweight CLI workflow.</li>
  <li>Includes sample CSV and JSON files for quick inspection.</li>
</ul>

## Tech Stack

<table>
  <tr><th>Layer</th><th>Tools</th></tr>
  <tr><td>Core stack</td><td>Python, argparse, csv, json</td></tr>
  <tr><td>Supporting tools</td><td>pathlib</td></tr>
</table>

## Quick Start

<pre><code>python csv_to_json.py sample_data.csv
python csv_to_json.py sample_data.csv -o sample_data.json --indent 4</code></pre>

## Project Structure

<pre>csv_to_json.py - CLI entry point and conversion logic
sample_data.csv - Small example input
sample_data.json - Example JSON output
asteroids.csv / asteroids.json - Larger sample conversion</pre>

## Validation

<p>
Run the CLI against <code>sample_data.csv</code> and compare the generated JSON output.
</p>

## Scope Notes

<p>
The converter assumes the first row contains headers and does not stream very large files chunk-by-chunk.
</p>

## Roadmap

<ul>
  <li>Add unit tests for type conversion edge cases.</li>
  <li>Support delimiter configuration for TSV or semicolon-separated files.</li>
</ul>

## License

<p>
No license file is currently included.
</p>

## Built By

<p>
Built by <strong>Abigail Briones Aranda</strong> as part of a growing AI/software engineering portfolio focused on readable systems, thoughtful interfaces, and reproducible project documentation.
</p>

</samp>
