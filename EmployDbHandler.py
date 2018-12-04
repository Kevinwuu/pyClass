import pickle
import os


class EmployDbHandler():
    def __init__(self):
        pass

    def check(self):
        # 檢查db檔存在
        if os.path.exists("EmployDb.dat"):
            return pickle._load(open('EmployDb.dat', 'rb'))
        else:
            empty_dict = dict()
            pickle._dump(empty_dict, open('EmployDb.dat', 'wb'))
            return empty_dict

    def add_modify_employee(self):
        pass

    def quitapp(self, employee_dict):
        pickle._dump(employee_dict, open('EmployDb.bat', 'wb'))
