from EmployeeClass import *


class ChangeEmployee():
    def __init__(self, ids):
        self.ids = ids

    def mod(self, id_em_dict):
        if self.ids in id_em_dict:
            if type(id_em_dict[self.ids] == WorkerClass):
                print(f'Current name is: {id_em_dict[self.ids].name}')
                id_em_dict[self.ids].name = input('Enter a new name: ')
                print(f'Current shift is: {id_em_dict[self.ids].shift}')
                id_em_dict[self.ids].shift = input('Enter a new shift: ')
                print(f'Current rate is: {id_em_dict[self.ids].rate}')
                id_em_dict[self.ids].rate = input('Enter a new rate.')
                print("Information updated!!!")
            else:
                print(f'Current name is: {id_em_dict[self.ids].name}')
                id_em_dict[self.ids].name = input('Enter a new name: ')
                print(f'Current salary is: {id_em_dict[self.ids].salary}')
                id_em_dict[self.ids].salary = input('Enter a new salary: ')
                print(f'Current bonus is: {id_em_dict[self.ids].bonus}')
                id_em_dict[self.ids].bonus = input('Enter a new bonus.')
                print("Information updated!!!")
        else:
            print('No such ID to modify employee information.')
