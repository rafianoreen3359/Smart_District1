""" Task:  Student Result Processor: The academic department has CSV files of student records 
in a folder. Some files are corrupted, some are missing, and some have invalid data. 
1Build a system that reads all files safely, flags failed students, and writes a clean results 
file without ever crashing."""

import os
import csv

results = []

base_folder = os.path.dirname(os.path.abspath(__file__))
students_folder = os.path.join(base_folder, "students")
output_file = os.path.join(base_folder, "clean_results.csv")

try:
    for filename in os.listdir(students_folder):

        if filename.endswith(".csv"):

            file_path = os.path.join(students_folder, filename)

            try:
                with open(
                    file_path, "r", newline="", encoding="utf-8-sig"
                ) as file:

                    reader = csv.DictReader(file)

                    if not reader.fieldnames or not {
                        "name", "marks"
                    }.issubset(reader.fieldnames):
                        print("Invalid CSV format:", filename)
                        continue

                    for row in reader:
                        try:
                            name = (row.get("name") or "").strip()
                            marks_text = (row.get("marks") or "").strip()

                            if not name or not marks_text:
                                raise ValueError("Missing name or marks")

                            marks = int(marks_text)

                            if marks < 0 or marks > 100:
                                print("Invalid marks:", name)
                                continue

                            if marks < 50:
                                status = "Fail"
                            else:
                                status = "Pass"

                            results.append([name, marks, status])

                        except (ValueError, TypeError, AttributeError):
                            print("Invalid student record:", row)

            except (OSError, csv.Error, UnicodeError) as error:
                print("File error:", filename, error)

except OSError as error:
    print("Folder error:", error)

try:
    with open(
        output_file, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Status"])
        writer.writerows(results)

    print("Results saved successfully!")
    print("Total valid records:", len(results))

except OSError as error:
    print("Could not save results:", error)
