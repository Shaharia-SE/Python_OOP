"""
Your best friend is founding a startup and he desperately needs your help to implement
a payroll system. The developer he hired last month only completed part of the program
because he had a medical emergency and had to quit the job before completing it.
 Your job is to complete the classes in the existing payroll system by including
the necessary class attributes.
 First, you need to analyze the “payroll” function located at the bottom of the file
(or in the code below). From that code, you need to determine the attributes
that the classes require. After meeting with your friend, you have determined
that these attributes are shared by all instances of the classes, so they will be
class attributes.
 Assign realistic values to them.
 Submit your code and the program output displayed after running it to complete
this mini project
"""
class Programmer:
    salary = 15000
    monthly_bonus = 300


    # Add the class attributes

    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages


class Assistant:
    salary = 15000
    monthly_bonus = 300

    # Add the class attributes

    def __init__(self, name, age, address, phone, bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.bilingual = bilingual


# Program ==================================================================

# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month
def calculate_payroll(employees):
    total = 0

    print("\n========= Welcome to our Payroll System =========\n")

    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary

    # Display the total
    print("\nThe total payroll this month will be: $", total)


# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)

# List of instances
employees = [jack, isabel, nora]

# Function call - Passing the list of instances as argument
calculate_payroll(employees)
