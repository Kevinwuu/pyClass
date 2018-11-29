from EmployeeClass import *


class DelEmployee():
    def __init__(self, ids):
        self.ids = ids

    def delete(self, id_em_dict):
        if self.ids in id_em_dict:
            del(id_em_dict[self.ids])
        else:
            print('No such ID to delete!!!')
