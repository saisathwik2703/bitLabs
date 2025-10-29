import math
import sys

class Student:
    """
    Implements the Student class to manage individual student data.
    It calculates and stores the student's average mark upon initialization.
    """
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks
        self.average = self._calculate_average()

    def _calculate_average(self) -> float:
        """
        Calculates the average mark for the student.
        Returns: The calculated average, rounded to two decimal places.
        """
        if not self.marks:
            return 0.0
        # Calculate average and round to two decimal places for required output format
        return round(sum(self.marks) / len(self.marks), 2)

    def get_average(self) -> float:
        """Returns the calculated average mark."""
        return self.average

def track_performance(students_data: dict) -> tuple[dict, str]:
    """
    Calculates the average marks for all students and identifies the top performer.

    Args:
        students_data: A dictionary where keys are student names (str) and
                       values are a list of marks (list[int]).

    Returns:
        A tuple containing:
        1. A dictionary of student names and their average marks.
        2. The name of the student with the highest average.
    """
    if not students_data:
        return {}, "No students tracked."

    student_objects = []
    average_marks = {}

    # 1. Calculate all averages and store student objects
    for name, marks in students_data.items():
        student = Student(name, marks)
        student_objects.append(student)
        average_marks[name] = student.get_average()

    # 2. Identify the top performer
    top_performer = ""
    highest_average = -1.0

    for student in student_objects:
        if student.average > highest_average:
            highest_average = student.average
            top_performer = student.name
        # Note: If averages are tied, the first student encountered with that average remains the top performer.

    return average_marks, top_performer

# Main execution block
if __name__ == "__main__":
    print("--- Classroom Performance Tracker ---")

    # Input Example
    initial_students = {
        "John": [85, 78, 92], 
        "Alice": [88, 79, 95], 
        "Bob": [70, 75, 80]
    }
    
    print("\nStudent Data Being Processed:")
    for name, marks in initial_students.items():
        print(f"  - {name}: {marks}")

    # Calculate and find top performer
    averages, top_student = track_performance(initial_students)

    # Output the results
    print("\n--- Performance Report ---")
    print(f"Average Marks: {averages}")
    print(f"Top Performer: \"{top_student}\"")
    print("--------------------------")