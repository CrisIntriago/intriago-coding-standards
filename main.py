"""
Module defining the Student class for managing students and their grades,
along with a demonstration function start_run() that showcases basic usage.
"""
from typing import List


class Student:
    """
    Represents a student with an ID, name, grades, honor status, and letter grade.
    Attributes:
        student_id (int): The unique identifier for the student.
        name (str): The name of the student.
        grades (list): A list of grades associated with the student.
        honor (bool): Indicates if the student has honor status based on their average grade.
        letter (str): The final letter grade for the student.
    Methods:
        add_grades(grade):
        calc_average():
            Calculates and returns the average of the student's grades.
        check_honor():
            Determines if the student qualifies for honor status based on their average grade.
        delete_grade(index):
        report():
    """

    def __init__(self, student_id: int = None,  name: str = None):
        if not student_id:
            print("Error: student_id must not be empty or zero. Setting to default 0.")
            self.student_id = 0
        else:
            self.student_id = student_id

        if not name or name.strip() == "":
            print("Error: name must not be empty. Setting to 'Unknown'.")
            self.name = "Unknown"
        else:
            self.name = name.strip()
        self.grades: List[float] = []
        self.honor = False
        self.pass_status = False

    def add_grades(self, grade: float):
        """
        Adds a grade to the student's list of grades after validating it is
        within 0 to 100 inclusive.

        Args:
            grade (float): The grade to be added.

        Raises:
            ValueError: If the grade is not between 0 and 100.
        """
        if not 0 <= grade <= 100:
            raise ValueError(
                f"Invalid grade {grade}. Grade must be between 0 and 100.")
        self.grades.append(grade)

    def calc_average(self):
        """
        Calculates the average of the grades stored in the 'gradez' attribute.

        Returns:
            float: The average of the grades.

        Raises:
            ZeroDivisionError: If the number of grades is zero.
        """
        total = 0
        for grade in self.grades:
            total += grade
        if len(self.grades) == 0:
            raise ZeroDivisionError(
                "No grades available to calculate average.")
        return total/len(self.grades)

    def determine_letter(self, grade: float) -> str:
        """
        Converts a numeric average into a letter grade.

        Ranges:
            A: 90–100
            B: 80–89
            C: 70–79
            D: 60–69
            F: <60

        Args:
            grade (float): Numeric average.

        Returns:
            str: Corresponding letter grade.
        """
        self.pass_status = grade >= 60
        if 90 <= grade <= 100:
            return "A"
        if 80 <= grade < 90:
            return "B"
        if 70 <= grade < 80:
            return "C"
        if 60 <= grade < 70:
            return "D"
        return "F"

    def check_honor(self):
        """
        Determines if the honor attribute should be set based on the student's average grade.

        Calls the calc_average() method and, if the result is greater than 90, sets the honor attribute to "yep".
        """
        self.honor = self.calc_average() > 90

    def delete_grade(self, identifier):
        """
        Removes a grade from the grades list by value or by index.

        Args:
            identifier (int or float): If int, treated as index to remove.
                                    If float, treated as grade value to remove.

        Behavior:
            - If index is out of range, prints an error message.
            - If value not found in grades, prints an error message.
        """
        if isinstance(identifier, int):
            # Remove by index
            try:
                removed = self.grades.pop(identifier)
                print(f"Removed grade {removed} at index {identifier}.")
            except IndexError:
                print(
                    f"Error: Index {identifier} is out of range for grades list.")
        elif isinstance(identifier, (float, int)):
            # Remove by value (allow int grades too)
            try:
                self.grades.remove(float(identifier))
                print(f"Removed grade value {identifier}.")
            except ValueError:
                print(
                    f"Error: Grade value {identifier} not found in grades list.")
        else:
            print("Error: Identifier must be an integer index or a float grade value.")

    def report(self):
        """
        Prints a report of the student's information, including ID, name, number of grades, and final letter grade.

        Note:
            - Assumes the instance has attributes: id (str), name (str), grades (iterable), and letter (str).
            - The method prints the information to the standard output.
        """
        print("ID: " + str(self.student_id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Letter Grade = " + self.determine_letter(self.calc_average()))
        print("Average Grade = " + str(self.calc_average()))
        print("Honor: " + ("Yes" if self.honor else "No"))
        print("The student is passed" if self.pass_status else "He is not passed")


def start_run():
    """
    Executes a sequence of operations on a student object to demonstrate grade management functionality.

    The function performs the following actions:
    1. Creates a student instance with a placeholder name and empty ID.
    2. Adds a valid grade (integer).
    3. Attempts to add an invalid grade (string), which may cause an error.
    4. Calculates the student's average grade.
    5. Checks if the student qualifies for honors.
    6. Attempts to delete a grade at an invalid index, which may raise an IndexError.
    7. Generates a report of the student's grades and status.

    Note:
    - This function is intended for demonstration or testing purposes and may raise exceptions due to invalid operations.
    """
    a = Student(1290, "Cristian Intriago")
    a.add_grades(100)
    a.add_grades(50)
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)
    a.report()


start_run()
