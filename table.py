from prettytable import PrettyTable


class Table:
    def __init__(self):
        self.item_name = ['index', 'name', 'qq', 'telephone', 'email']
        self.student_list = []

    def add(self, student):
        self.student_list.append(student)

    def modify(self, index):
        self.student_list[index].modify()

    def delete(self, index):
        self.student_list.pop(index)

    def all_student(self):
        t = PrettyTable()
        t.field_names = self.item_name
        for index, stu in enumerate(self.student_list):
            t.add_row([index+1, *stu.student_info.values()] )
        print(t)

    def operate(self, op):
        if op == 'a':
            self.add_handler()
        elif op == 's':
            self.search_handler()
        elif op == 'd':
            self.delete_handler()
        elif op == 'm':
            self.modify_handler()

    def add_handler(self):
        print('Please input the message of new student')
        stu = []
        for index, field in enumerate(self.item_name):
            if index == 0:
                continue
            while True:
                value = input('Please input %s: ' % field)
                if value:
                    stu.append(value)
                    break
                else:
                    continue
        self.add(Student(stu))

    def search_handler(self):
        self.all_student()

    def modify_handler(self):
        index = input('please input the index of line you want to modify: ')
        try:
            index = int(index) - 1
            if index < len(self.student_list):
                self.modify(index)
            else:
                print('line out of bound')
        except ValueError as e:
            print('please input a number')




    def delete_handler(self):
        index = input('please input the index of line you want to delete: ')
        try:
            index = int(index) - 1
            if index < len(self.student_list):
                self.delete(index)
            else:
                print('line out of bound')
        except ValueError as e:
            print('please input a number')
