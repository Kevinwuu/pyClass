from EmployeeClass import *


class AddEmployee():
    def __init__(self):
        self.ids = input("Plz enter the employee ID: ")
        self.name = input("The employee name: ")
        self.Etype = input("Type (1) Worker (2) Supervisor: ")
        if self.Etype == '1':
            self.shift = input("Shift (1) day (2) night: ")
            self.rate = input("Rate: ")
        else:
            self.salary = input("Salary: ")
            self.bonus = input("Bonus: ")

    def register(self, id_em_dict):
        if self.ids in id_em_dict:
            print("這個ID有了，不能新增")
        else:
            if self.Etype == "1":
                id_em_dict[self.ids] = WorkerClass(
                    self.name, self.ids, self.Etype, self.shift, self.rate)
            else:
                id_em_dict[self.ids] = SupervisorClass(
                    self.name, self.ids, self.Etype, self.salary, self.bonus)
