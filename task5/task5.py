""" ● HR Employee Ranker: HR wants employees ranked by performance score, then by experience as a tiebreaker, then by name alphabetically. The system must also support quickly searching for a specific employee by name from the sorted list."""

employees = [
    {"name": "Ali", "score": 85, "experience": 3},
    {"name": "Sara", "score": 95, "experience": 5},
    {"name": "Ahmed", "score": 85, "experience": 5},
    {"name": "Ayesha", "score": 95, "experience": 3},
    {"name": "Bilal", "score": 85, "experience": 5},
]

ranked_employees = sorted(
    employees,
    key=lambda e: (-e["score"], -e["experience"], e["name"].lower())
)

for rank, employee in enumerate(ranked_employees, start=1):
    print(
        rank,
        employee["name"],
        "Score:", employee["score"],
        "Experience:", employee["experience"]
    )

search_name = input("\nEnter employee name to search: ").strip().lower()

found_employee = next(
    (e for e in ranked_employees
     if e["name"].lower() == search_name),
    None
)

if found_employee:
    print("Employee found:", found_employee)
else:
    print("Employee not found.")
