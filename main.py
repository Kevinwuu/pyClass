from AddEmployee import *
from ChangeEmployee import *
from DelEmployee import *
from EmployDbHandler import *
from EmployeeClass import *
from ListAllEmployee import *
from LookUpEmployee import *


# var
choice = ""
employee_dict = dict()
command_dict = {
    "0": "Quit the program",
    "1": "Add a new employee",
    "2": "List all",
    "3": "Look up a employee",
    "4": "Change a existing employee",
    "5": "Deltet the Employee"
}


# 選單
for i in command_dict:
    print(f'{i}. {command_dict[i]}')
choice = input('Plz input your choice')

while choice != "0":
    if choice == "1":
        AddEmployee().register(employee_dict)
    elif choice == "2":
        ListAllEmployee().ls(employee_dict)
    elif choice == '3':
        temp_id = input("Looking up ID: ")
        LookUpEmployee(temp_id).find(employee_dict)
    elif choice == '4':
        temp_id = input("Want to modify ID: ")
        ChangeEmployee(temp_id).mod(employee_dict)
    else:
        temp_id = input("Want to del ID: ")
        DelEmployee(temp_id).delete(employee_dict)

    for i in command_dict:
        print(f'{i}. {command_dict[i]}')
    choice = input('Plz input your choice')
