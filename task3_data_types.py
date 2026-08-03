Task 3: Python Data Types
Demonstrates int, float, bool, string, list, tuple, set, dict and
type casting.
"""
 
 
def demo_int():
    """(a) Integer variable and type() check."""
    age = 25
    print("Integer value:", age)
    print("Type:", type(age))
 
 
def demo_float():
    """(b) Float variable and arithmetic."""
    price = 49.99
    quantity = 3.0
    total = price * quantity
    print("Float value:", price)
    print("Total (price * quantity):", total)
 
 
def demo_boolean():
    """(c) Boolean variable used in a conditional."""
    is_registered = True
    if is_registered:
        print("Status: Student is registered.")
    else:
        print("Status: Student is not registered.")
 
 
def demo_string():
    """(d) String concatenation, slicing and len()."""
    first_name = "John"
    last_name = "Otieno"
    full_name = first_name + " " + last_name  # concatenation
    print("Full name:", full_name)
    print("First 4 characters:", full_name[:4])   # slicing
    print("Length of full name:", len(full_name))  # len()
 
 
def demo_list():
    """(e) List with append(), remove() and indexing."""
    fruits = ["mango", "banana", "apple", "orange", "grapes"]
    print("Original list:", fruits)
 
    fruits.append("pineapple")
    print("After append:", fruits)
 
    fruits.remove("banana")
    print("After remove:", fruits)
 
    print("Item at index 0:", fruits[0])
 
 
def demo_tuple():
    """(f) Tuple immutability demonstrated with a try/except."""
    coordinates = (36.8219, -1.2921)
    print("Tuple:", coordinates)
    try:
        coordinates[0] = 0  # this will raise a TypeError
    except TypeError as error:
        print("Cannot modify tuple:", error)
 
 
def demo_set():
    """(g) Set removes duplicate values automatically."""
    numbers = {1, 2, 2, 3, 4, 4, 5}
    print("Set (duplicates removed):", numbers)
 
 
def demo_dict():
    """(h) Dictionary: access, add and delete a key."""
    student = {
        "name": "Grace Wanjiru",
        "age": 22,
        "course": "Computer Science",
    }
    print("Original dictionary:", student)
 
    print("Accessing 'name':", student["name"])
 
    student["year"] = 3  # add a new key
    print("After adding 'year':", student)
 
    del student["age"]  # delete a key
    print("After deleting 'age':", student)
 
 
def demo_type_casting():
    """(i) Type casting between int, float and str."""
    text_number = "10"
    number = int(text_number)          # str -> int
    decimal = float(number)            # int -> float
    back_to_text = str(decimal)        # float -> str
 
    print("Original string:", text_number, type(text_number))
    print("As int:", number, type(number))
    print("As float:", decimal, type(decimal))
    print("Back to string:", back_to_text, type(back_to_text))
 
 
def main():
    demo_int()
    print()
    demo_float()
    print()
    demo_boolean()
    print()
    demo_string()
    print()
    demo_list()
    print()
    demo_tuple()
    print()
    demo_set()
    print()
    demo_dict()
    print()
    demo_type_casting()
 
 
if __name__ == "__main__":
    main()
