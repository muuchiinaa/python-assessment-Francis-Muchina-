Task 2: Python Syntax, Zen of Python & PEP 8
 
Zen of Python - two principles explained (from `import this`):
 
1. "Beautiful is better than ugly."
   Code should be written in a clean, readable way rather than a messy
   or clever-but-confusing way. Readable code is easier to maintain,
   debug and share with others.
 
2. "Simple is better than complex."
   When there are two ways to solve a problem, prefer the simpler one.
   Simple code has fewer places for bugs to hide and is easier for
   other programmers (or future you) to understand quickly.
"""
 
# (a) Two Zen of Python principles are explained in the module docstring
#     above, as required by the task.
 
 
# (b)-(e) A PEP 8 compliant script below
 
def main():
    """Demonstrate PEP 8 style and basic variable assignment."""
    # (d) & (e) Three different variable assignments using snake_case
    student_name = "Asha Mwangi"          # string assignment
    student_age = 21                      # integer assignment
    is_full_time = True                   # boolean assignment
 
    # (c) Single-line comment: print a short, clean summary
    print("Student Record")
    print("-" * 20)
    print(f"Name       : {student_name}")
    print(f"Age        : {student_age}")
    print(f"Full-time  : {is_full_time}")
 
    # A second block of assignments to further demonstrate style
    subjects_taken = 5
    average_score = 82.5
    print(f"Subjects   : {subjects_taken}")
    print(f"Average    : {average_score}")
 
 
if __name__ == "__main__":
    main()
