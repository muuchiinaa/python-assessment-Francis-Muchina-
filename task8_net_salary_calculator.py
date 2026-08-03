HOUSE_ALLOWANCE = 6500
MEDICAL_ALLOWANCE = 5500
 
def get_employee_details():
    """(a) Capture employee details."""
    payroll_number = input("Enter payroll number: ")
    name = input("Enter employee name: ")
    gender = input("Enter gender: ")
    department = input("Enter department: ")
    basic_salary = float(input("Enter basic salary (Ksh): "))
    return payroll_number, name, gender, department, basic_salary
 
 
def calculate_gross_pay(basic_salary):
    """(b) Gross pay = Basic Salary + House Allowance + Medical Allowance."""
    return basic_salary + HOUSE_ALLOWANCE + MEDICAL_ALLOWANCE
 
 
def calculate_paye(gross_pay):
    """(c) Calculate PAYE using a simple bracketed rate structure."""
    if gross_pay <= 15000:
        rate = 0.00
    elif gross_pay <= 30000:
        rate = 0.04
    elif gross_pay <= 50000:
        rate = 0.05
    else:
        rate = 0.06
    return gross_pay * rate
 
 
def calculate_nhif(gross_pay):
    """(d) NHIF = 2% of gross pay."""
    return gross_pay * 0.02
 
 
def calculate_nssf(basic_salary):
    """(d) NSSF = 3% of basic salary."""
    return basic_salary * 0.03
 
 
def calculate_net_pay(gross_pay, paye, nhif, nssf):
    """(e) Total deductions and net pay."""
    total_deductions = paye + nhif + nssf
    net_pay = gross_pay - total_deductions
    return total_deductions, net_pay
 
 
def display_payslip(payroll_number, name, gender, department,
                     basic_salary, gross_pay, paye, nhif, nssf,
                     total_deductions, net_pay):
    """(f) Display all employee details and salary breakdown."""
    print("\n" + "=" * 40)
    print("           EMPLOYEE PAYSLIP")
    print("=" * 40)
    print(f"Payroll Number   : {payroll_number}")
    print(f"Name             : {name}")
    print(f"Gender           : {gender}")
    print(f"Department       : {department}")
    print("-" * 40)
    print(f"Basic Salary     : Ksh {basic_salary:,.2f}")
    print(f"House Allowance  : Ksh {HOUSE_ALLOWANCE:,.2f}")
    print(f"Medical Allowance: Ksh {MEDICAL_ALLOWANCE:,.2f}")
    print(f"Gross Pay        : Ksh {gross_pay:,.2f}")
    print("-" * 40)
    print(f"PAYE             : Ksh {paye:,.2f}")
    print(f"NHIF (2% gross)  : Ksh {nhif:,.2f}")
    print(f"NSSF (3% basic)  : Ksh {nssf:,.2f}")
    print(f"Total Deductions : Ksh {total_deductions:,.2f}")
    print("-" * 40)
    print(f"NET PAY          : Ksh {net_pay:,.2f}")
    print("=" * 40)
 
 
def main():
    (payroll_number, name, gender,
     department, basic_salary) = get_employee_details()
 
    gross_pay = calculate_gross_pay(basic_salary)
    paye = calculate_paye(gross_pay)
    nhif = calculate_nhif(gross_pay)
    nssf = calculate_nssf(basic_salary)
    total_deductions, net_pay = calculate_net_pay(
        gross_pay, paye, nhif, nssf
    )
 
    display_payslip(
        payroll_number, name, gender, department, basic_salary,
        gross_pay, paye, nhif, nssf, total_deductions, net_pay
    )
 
 
if __name__ == "__main__":
    main()
