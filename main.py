name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks < 90:
    grade = "B"
elif 50 <= marks < 75:
    grade = "C"
elif 0 <= marks < 50:
    grade = "D"
else:
    grade = "Invalid marks"

print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
