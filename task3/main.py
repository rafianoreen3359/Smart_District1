"""Task: 
● Project Directory Auditor: The DevOps team needs a tool that scans a given project folder, collects each file's name, size, type, and last modified date, then generates a timestamped audit report. Files not modified in over 30 days must be flagged, and a separate penalties report must list any calculated overage fines. Package the scanning logic as a custom importable module that the audit script imports and uses."""


import os
import csv
from datetime import datetime
from auditor import scan_files

folder = "my_project"

os.makedirs(folder, exist_ok=True)

test_path = os.path.join(folder, "test.txt")

with open(test_path, "w", encoding="utf-8") as f:
    f.write("Hello Python")

results = scan_files(folder)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

with open(
    f"audit_{timestamp}.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:
    fields = ["name", "size", "type", "modified", "status", "fine"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)
with open(
    f"penalties_{timestamp}.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:
    fields = ["name", "fine"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for item in results:
        if item["status"] == "OLD":
            writer.writerow({
                "name": item["name"],
                "fine": item["fine"]
            })

print("Audit report created successfully!")
print("Total files:", len(results))
