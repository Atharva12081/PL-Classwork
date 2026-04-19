"""
Assignment 8: Convert student records from JSON to CSV.

Reads:  students.json (list of objects with keys: name, section, age, marks)
Writes: Student.csv in this folder (regenerated when you run the script)

This assignment does not share files with any other assignment.
"""
import csv
import json
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__).resolve().parent
JSON_PATH = ASSIGNMENT_DIR / "students.json"
CSV_PATH = ASSIGNMENT_DIR / "Student.csv"


def json_records_to_csv() -> None:
    if not JSON_PATH.is_file():
        raise SystemExit(
            f"Missing input file: {JSON_PATH}\n"
            "Add students.json with a list of student objects."
        )

    with JSON_PATH.open("r", encoding="utf-8") as json_handle:
        records = json.load(json_handle)

    if not isinstance(records, list) or not records:
        raise SystemExit("students.json must contain a non-empty list of records.")

    if not isinstance(records[0], dict):
        raise SystemExit("Each record in students.json must be an object (dictionary).")

    column_names = list(records[0].keys())

    with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_handle:
        writer = csv.DictWriter(csv_handle, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(records)

    print(f"Wrote {len(records)} row(s) to {CSV_PATH.name}")


if __name__ == "__main__":
    json_records_to_csv()
