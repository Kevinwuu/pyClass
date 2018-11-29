from EmployeeClass import *


class ListAllEmployee():
    def __init__(self):
        pass

    def ls(self, id_em_dict):
        for each in id_em_dict:
            if type(id_em_dict[each]) == WorkerClass:  # 加入時是一般worker
                print(f'員工ID: {each}\n' +
                      f'員工姓名: {id_em_dict[each].name}\n' +
                      f'員工身分: 普通員工\n' +
                      f'員工shift: {id_em_dict[each].shift}\n' +
                      f'員工rate: {id_em_dict[each].rate}\n')
            elif type(id_em_dict[each]) == SupervisorClass:  # 加入時是領班員工
                print(f'員工ID: {each}\n' +
                      f'員工姓名: {id_em_dict[each].name}\n' +
                      f'員工身分: 領班員工\n' +
                      f'員工salary: {id_em_dict[each].salary}\n' +
                      f'員工bonus: {id_em_dict[each].bonus}\n')
