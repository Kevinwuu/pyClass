from EmployeeClass import WorkerClass


class LookUpEmployee():
    def __init__(self, ids):
        self.ids = ids

    def find(self, id_em_dict):
        if self.ids in id_em_dict:
            if type(id_em_dict[self.ids]) == WorkerClass:
                print(f'員工ID: {self.ids}\n' +
                      f'員工姓名: {id_em_dict[self.ids].name}\n' +
                      f'員工身分: 普通員工\n' +
                      f'員工排班: {id_em_dict[self.ids].shift}\n' +
                      f'員工時薪: {id_em_dict[self.ids].rate}\n')
            else:
                print(f'員工ID: {self.ids}\n' +
                      f'員工姓名: {id_em_dict[self.ids].name}\n' +
                      f'員工身分: 領班員工\n' +
                      f'員工排班: {id_em_dict[self.ids].salary}\n' +
                      f'員工時薪: {id_em_dict[self.ids].bonus}\n')
        else:
            print('Look up fail! No such employee!')
