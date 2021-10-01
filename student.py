class Student:
    def __init__(self, stu):
        name, qq, telephone, email = stu
        self.item_value = [name, qq, telephone, email]
        self.student_info = {
            'name':name,
            'qq':qq,
            'telephone':telephone,
            'email':email
        }

    def print_info(self):
        for value in self.student_info.values():
            print('\t',value,end='')

    def modify(self):
        print('Please input your modified message, press whitespace if ignore ')
        for item_name in self.student_info:
            print(item_name, ': ')
            modified_message = input()
            if modified_message in [' ', '']:
                continue
            else:
                self.student_info[item_name] = modified_message
