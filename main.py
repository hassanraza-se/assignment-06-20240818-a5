# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def manage_student_database():
    students = []
    student_names = set()
    student_id = 1

    while True:
        student_name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        if student_name.lower() == 'stop':
            break
        if student_name in student_names:
            print("This name is already in the list.")
        else:
            student_names.add(student_name)
            students.append((student_id, student_name))
            student_id += 1

    # Displaying the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Displaying each student's ID and name
    print("\nList of Students with IDs:")
    for student_id, name in students:
        print(f"ID: {student_id}, Name: {name}")

    # Calculating the total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculating the total length of all student names combined
    total_length = sum(len(name) for _, name in students)
    print(f"Total length of all student names combined: {total_length}")

    # Identifying the student with the longest and shortest name
    if students:
        longest = max(students, key=lambda x: len(x[1]))
        shortest = min(students, key=lambda x: len(x[1]))
        print(f"The student with the longest name is: {longest[1]}")
        print(f"The student with the shortest name is: {shortest[1]}")

if __name__ == '__main__':
    manage_student_database()
