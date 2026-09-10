# rpa-trainee-sruthyr

Day 1 — RPA Concepts + Python Refresher (07-09-2026)

Learn: What is RPA, where it's used, attended vs unattended bots, typical bot lifecycle (input → process → action → output → log). Python refresher: functions, f-strings, exception handling (try/except/finally), file I/O.
Hands-on: Write a script that reads a .txt log file, filters lines containing "ERROR", and writes them to a new file. Wrap all file operations in try/except.
Deliverable: week1/day1_log_filter.py + a 1-paragraph note in docs/rpa_concepts.md explaining RPA in the trainee's own words.

Day 2 — OOP for Bots + Logging (08-09-2026)

Learn: Classes/objects, __init__, methods, why bots are usually structured as classes (Bot, Config, ExcelHandler). Python's logging module (levels, file handlers, formatting).
Hands-on: Build a Logger utility class that writes timestamped logs to both console and a .log file. Reuse it in Day 1's script.
Deliverable: week1/logger_utils.py

Day 3 — openpyxl Basics  (09-09-2026)

Learn: Workbooks, worksheets, reading/writing cells, iterating rows/columns, load_workbook, saving files, handling .xlsx vs .xls.
Hands-on: Create an Excel file with 20 dummy invoice records (Invoice ID, Customer, Amount, Date, Status). Write a script to read it and print each row as a dictionary.
Deliverable: week1/day3_read_excel.py + sample_data/invoices.xlsx

Day 4 - openpyxl Advanced + pandas for Data Handling   (10-09-2026)

Learn: Cell styling (fonts, fills, borders), formulas, multiple sheets, merging cells. Intro to pandas (read_excel, DataFrame filtering, to_excel) as a faster alternative for bulk data work.
Hands-on: Read invoices.xlsx, filter records where Amount > 5000, highlight those rows in yellow, and write a summary sheet (Total, Count, Average).
Deliverable: week1/day4_excel_report.py


