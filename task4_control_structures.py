task4_control_structures.py
 
Task 4: Control Structures - Selection & Looping
"""
 
 
def classify_grade(marks):
    """(a) Classify a student's grade using if-elif-else."""
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Marks: {marks} -> Grade: {grade}")
    return grade
 
 
def print_fruits():
    """(b) For loop over a list of 5 fruits."""
    fruits = ["mango", "banana", "apple", "orange", "grapes"]
    for fruit in fruits:
        print(fruit)
 
 
def print_even_numbers():
    """(c) While loop that prints even numbers from 1 to 10."""
    number = 1
    while number <= 10:
        if number % 2 == 0:
            print(number)
        number += 1
 
 
def break_continue_demo():
    """(d) Demonstrate break and continue in a practical example."""
    print("Searching for the first number divisible by 7:")
    for number in range(1, 50):
        if number % 7 != 0:
            continue  # skip numbers not divisible by 7
        print(f"Found it: {number}")
        break  # stop once the first match is found
 
 
def multiplication_table():
    """(e) Nested loop printing a 3x3 multiplication table."""
    for row in range(1, 4):
        line = ""
        for col in range(1, 4):
            product = row * col
            line += f"{product:4}"
        print(line)
 
 
def main():
    classify_grade(85)
    classify_grade(45)
    print()
 
    print_fruits()
    print()
 
    print_even_numbers()
    print()
 
    break_continue_demo()
    print()
 
    multiplication_table()
 
 
if __name__ == "__main__":
    main()
