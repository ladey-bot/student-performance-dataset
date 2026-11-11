import csv

# Create a fictional student dataset
students = [
    ["Student ID", "Department", "Level",
     "Attendance Percentage", "Average Examination Score"],

    ["ST001", "Computer Science", 300, 85, 78],
    ["ST002", "Cyber Security", 200, 90, 85],
    ["ST003", "Information Technology", 300, 75, 68],
    ["ST004", "Computer Science", 100, 80, 72],
    ["ST005", "Software Engineering", 400, 95, 91],
    ["ST006", "Cyber Security", 200, 70, 65],
    ["ST007", "Computer Science", 300, 88, 82],
    ["ST008", "Data Science", 100, 92, 88],
    ["ST009", "Information Technology", 400, 78, 70],
    ["ST010", "Software Engineering", 200, 85, 79],
    ["ST011", "Computer Science", 100, 65, 60],
    ["ST012", "Cyber Security", 300, 90, 86],
    ["ST013", "Data Science", 200, 82, 75],
    ["ST014", "Information Technology", 400, 96, 93],
    ["ST015", "Computer Science", 300, 87, 84],
    ["ST016", "Software Engineering", 100, 73, 67],
    ["ST017", "Cyber Security", 200, 89, 81],
    ["ST018", "Data Science", 400, 94, 90],
    ["ST019", "Computer Science", 300, 80, 74],
    ["ST020", "Information Technology", 200, 76, 69]
]

# Save the dataset as a CSV file
with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

# Display the dataset
print("STUDENT PERFORMANCE DATASET")

for student in students:
    print(student)

print("\nDataset successfully saved!")