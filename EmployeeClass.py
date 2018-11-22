class EmployeeClass():
    def __init__(self, name, ids, Etype):
        self.name = name
        self.ids = ids
        self.Etype = Etype

    def __str__(self):
        return('員工姓名:'+self.name +
               "\nID:"+self.ids +
               "\nType:"+self.Etype)


class WorkerClass(EmployeeClass):
    def __init__(self, name, ids, Etype, shift, rate):
        super(WorkerClass, self).__init__(name, ids, Etype)
        self.shift = shift
        self.rate = rate

    def __str__(self):
        return(f'普通員工姓名:{self.name}\nID:{self.ids}\nType:{self.Etype}\n排班:{self.shift}\n時薪:{self.rate}')


class SupervisorClass(EmployeeClass):
    def __init__(self, name, ids, Etype, salary, bonus):
        super(SupervisorClass, self).__init__(name, ids, Etype)
        self.salary = salary
        self.bonus = bonus

    def __str__(self):
        return(f'領班員工姓名:{self.name}\nID:{self.ids}\nType:{self.Etype}\n薪資:{self.salary}\n獎金:{self.bonus}')
