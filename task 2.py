# Task 1: Store marks and calculate total & average
marks = [
    [85, 90, 78],  
    [76, 88, 85], 
    [90, 92, 94]   
]

print("Task 1: Total and Average Marks")
for i, student_marks in enumerate(marks):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i+1}: Total = {total}, Average = {average:.2f}")
print()

# Task 2: Store student data as tuples
students = [
    (101, "Alice", 17),
    (102, "Bob", 18),
    (103, "Charlie", 17)
]

print("Task 2: Student Information")
for roll, name, age in students:
    print(f"Roll No: {roll}, Name: {name}, Age: {age}")
print()

# Task 3: Dictionary and search function
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

def search_student(roll_no):
    return student_dict.get(roll_no, "Student not found")

print("Task 3: Search Student by Roll Number")
print("Search Roll No 102:", search_student(102))
print("Search Roll No 104:", search_student(104))
print()

# Task 4: Sets and set operations
football = {"Alice", "Bob"}
cricket = {"Bob", "Charlie"}
all_students = {"Alice", "Bob", "Charlie", "David"}  

both = football & cricket
only_one = (football ^ cricket)
none = all_students - (football | cricket)

print("Task 4: Sports Participation")
print("Play both football and cricket:", both)
print("Play only one sport:", only_one)
print("Play neither sport:", none)
