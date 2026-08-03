def welcome_message():
    """(a) Display a welcome message."""
    print("=" * 45)
    print("   WELCOME TO JESHI HOSPITAL")
    print("   Symptom-Based Diagnosis Assistant")
    print("=" * 45)
 
 
def get_patient_details():
    """(b) Capture patient details."""
    name = input("Enter patient name: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    residence = input("Enter place of residence: ")
    return name, gender, age, residence
 
 
def get_symptoms():
    """(c) Capture two symptoms from the user."""
    symptom_1 = input("Enter Symptom 1: ").strip().lower()
    symptom_2 = input("Enter Symptom 2: ").strip().lower()
    return symptom_1, symptom_2
 
 
def diagnose(symptom_1, symptom_2):
    """(d) & (e) Match symptom pairs to a diagnosis, or flag unknowns."""
    key = tuple(sorted([symptom_1, symptom_2]))
    return DIAGNOSIS_TABLE.get(key, None)
 
 
def display_result(name, symptom_1, symptom_2, diagnosis):
    """(f) Display formatted output of symptoms and diagnosis."""
    print("\n" + "-" * 45)
    print(f"Patient           : {name}")
    print(f"Symptom 1         : {symptom_1}")
    print(f"Symptom 2         : {symptom_2}")
    if diagnosis:
        print(f"Likely Diagnosis  : {diagnosis}")
    else:
        # (e) unrecognized symptom combination
        print("Likely Diagnosis  : Not recognized.")
        print("Please consult a doctor for further examination.")
    print("-" * 45)
 
 
def main():
    welcome_message()
    name, gender, age, residence = get_patient_details()
    symptom_1, symptom_2 = get_symptoms()
    diagnosis = diagnose(symptom_1, symptom_2)
    display_result(name, symptom_1, symptom_2, diagnosis)
 
 
if __name__ == "__main__":
    main()
