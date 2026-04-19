"""
Assignment 7 (Part 1): Text file write, append, and read.
All files for this assignment live in this folder only.
"""
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__).resolve().parent
TEXT_PATH = ASSIGNMENT_DIR / "lesson_notes.txt"

# Write initial content
with TEXT_PATH.open("w", encoding="utf-8") as out_stream:
    out_stream.write("Hello Students")

# Append additional line
with TEXT_PATH.open("a", encoding="utf-8") as out_stream:
    out_stream.write("\nWelcome to python")

# Read and display full contents
with TEXT_PATH.open("r", encoding="utf-8") as in_stream:
    contents = in_stream.read()
    print(contents)
