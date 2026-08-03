task5_functions.py
 
Task 5: Functions in Python
"""
 
total_calls = 0  # global variable used in the scope demo
 
 
def builtin_function_demo():
    """(a) Demonstrate len(), max() and sorted()."""
    scores = [67, 89, 45, 92, 78]
    print("Number of scores:", len(scores))
    print("Highest score:", max(scores))
    print("Sorted scores:", sorted(scores))
 
 
def calculate_area(length, width):
    """(b) Return the area of a rectangle."""
    return length * width
 
 
def greet(name, greeting="Hello"):
    """(c) Function with a default parameter value."""
    return f"{greeting}, {name}!"
 
 
def sum_all(*args):
    """(d) Accept a variable number of arguments and sum them."""
    return sum(args)
 
 
def lambda_demo():
    """(e) Lambda function to square numbers, used with map()."""
    numbers = [1, 2, 3, 4, 5]
    square = lambda x: x ** 2
    squared_numbers = list(map(square, numbers))
    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)
 
 
def scope_demo():
    """(f) Demonstrate local vs global variable scope."""
    global total_calls
    total_calls += 1  # modifies the global variable
 
    local_message = "I am local to scope_demo()"
    print(local_message)
    print("total_calls (global) is now:", total_calls)
 
 
def main():
    builtin_function_demo()
    print()
 
    area = calculate_area(5, 3)
    print(f"Area of rectangle (5 x 3): {area}")
    print()
 
    print(greet("Peter"))               # uses default greeting
    print(greet("Peter", "Good morning"))  # overrides default
    print()
 
    print("Sum of 1, 2, 3, 4:", sum_all(1, 2, 3, 4))
    print()
 
    lambda_demo()
    print()
 
    scope_demo()
    scope_demo()
 
 
if __name__ == "__main__":
    main()
