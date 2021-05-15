class Worker:
    def __init__(self, name, id, num_of_hour):
        self.name = name
        self.id = id
        self.num_of_hour = num_of_hour

    def zp(self, amount):
        self.amount = amount
        print(f'{self.id}: {self.name} - {self.amount}') 
        return self.amount

    def zp_kom(self, amount, count_of_sales):
        self.amount = amount
        self.kom = count_of_sales * 50
        self.am = self.amount + self.kom
        print(f'{self.id}: {self.name} - {self.am}')
        return self.am

    def zp_hour(self):
        self.one_hour = 100
        self.amm = self.num_of_hour*self.one_hour
        print(f'{self.id}: {self.name} - {self.amm}')
        return self.amm

    def productivity(self):
        return self.num_of_hour/40

    # def itogo_amount(self):
    #     for i in self.lst_of_amount:
    #         self.itogo += i
    #     return self.itogo

class Manager(Worker):
    pass
class Secretary(Worker):
    pass
class Saler(Worker):
    pass
class Worker_of_factory(Worker):
    pass
class Replacement_secretary(Worker):
    pass

class Itogo:
    def itogo_amount(self, *args):
        print(f'Итого у компании оплата труда составила {sum(args)}')

class Productivity:
    def prod(self, *args):
        self.lst = {}
        for i in args:
            self.lst[i.name] = i.productivity()
        self.sort_lst = sorted(self.lst.items(), key=lambda item: item[1])
        self.sort_dct = {k: v for k, v in self.sort_lst}
        print(f'Самый не продуктивный - {list(self.sort_dct)[0]}')
        print(f'Самый продуктивный - {list(self.sort_dct)[-1]}')

m = Manager('Barsbek Kanatkulov', 1, 18)
m_amount = m.zp(45000)

sec = Secretary('Alymkul Tilekbaev', 2, 38)
sec_amount = sec.zp(20000)

sal = Saler('Aiperi Shalymbekova', 3, 38)
sal_amount = sal.zp_kom(20000, 20)

worker1 = Worker_of_factory('Bakyt Rustamov', 4, 25)
worker1_amount = worker1.zp_hour()

worker2 = Worker_of_factory('Altynai Shirinbaeva', 5, 40)
worker2_amount = worker2.zp_hour()

rep_sec = Replacement_secretary('Janar Ryskulov', 6, 33)
rep_sec_amount = rep_sec.zp_hour()

i = Itogo()
i.itogo_amount(m_amount, sec_amount, sal_amount, worker1_amount, worker2_amount, rep_sec_amount)

p = Productivity()
p.prod(m, sec, sal, worker1, worker2, rep_sec)
