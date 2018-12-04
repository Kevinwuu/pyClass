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
    "1": AddEmployee,
    "2": ListAllEmployee,
    "3": LookUpEmployee,
    "4": ChangeEmployee,
    "5": DelEmployee
}


# 選單
for i in command_dict:
    print(f'{i}. {command_dict[i]}')
choice = input('Plz input your choice')

while choice != "0":
    if choice == "1":
        command_dict["1"]().register(employee_dict)
    elif choice == "2":
        command_dict["2"]().ls(employee_dict)
    elif choice == '3':
        temp_id = input("Looking up ID: ")
        command_dict["3"](temp_id).find(employee_dict)
    elif choice == '4':
        temp_id = input("Want to modify ID: ")
        command_dict["4"](temp_id).mod(employee_dict)
    else:
        temp_id = input("Want to del ID: ")
        command_dict["5"](temp_id).delete(employee_dict)

    for i in command_dict:
        print(f'{i}. {command_dict[i]}')
    choice = input('Plz input your choice')
