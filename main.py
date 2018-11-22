from EmployeeClass import *

# 以員工ID當作key
employee = dict()

control = input("1. Add a new employee" +
                "\n2. List all" +
                "\n0. Quit the program" +
                "\n Enter your choice:")

while int(control):
    if control == '1':  # add new employee
        e_ID = input("Plz enter the employee ID")
        e_name = input("Plz enter the employee name")
        e_type = input("1. Worker 2.Supervisor")
        if e_type == '1':  # type == worker
            e_shift = input("1.day 2.night")
            e_rate = input("Rate: ")
            employee[e_ID] = WorkerClass(e_name, e_ID, e_type, e_shift, e_rate)
        else:
            e_salary = input("Salary: ")
            e_bonus = input("Bonus: ")
            employee[e_ID] = SupervisorClass(e_name, e_ID, e_type, e_salary, e_bonus)

        print("The entry has been added")

    if control == '2':
        for i in employee:
            print(employee[i])

    control = input("1. Add a new employee" +
                    "\n2. List all" +
                    "\n0. Quit the program" +
                    "\n Enter your choice:")
