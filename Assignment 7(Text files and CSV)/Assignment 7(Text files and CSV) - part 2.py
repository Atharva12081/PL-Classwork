"""
Assignment 7 (Part 2): Create a CSV, then read it back row by row.
All files for this assignment live in this folder only.
"""
import csv
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__).resolve().parent
CSV_PATH = ASSIGNMENT_DIR / "marks_sheet.csv"

# Weekly quiz — "Intro to Python" cohort (sample scores out of 100)
header_row = ["Name", "Marks"]
sample_rows = [
    ["Priya Nair", "82"],
    ["Marcus Chen", "91"],
    ["Sofia Okonkwo", "76"],
    ["Diego Alvarez", "88"],
    ["Amara Osei", "94"],
    ["Yuki Tanaka", "79"],
]

with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_handle:
    sheet_writer = csv.writer(csv_handle)
    sheet_writer.writerow(header_row)
    sheet_writer.writerows(sample_rows)

with CSV_PATH.open("r", newline="", encoding="utf-8") as csv_handle:
    sheet_reader = csv.reader(csv_handle)
    for record in sheet_reader:
        print(record)
