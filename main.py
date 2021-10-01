
from student import Student
from table import Table


if __name__ == '__main__':
    p1 = ['wenbimig', 1233, 19080, '12@qq.com']
    p2 = ['WangJiaju', 12233, 190803, '123@qq.com']
    stu1 = Student(p1)
    stu2 = Student(p2)
    mytable = Table()
    mytable.add(stu1)
    mytable.add(stu2)


    mytable.all_student()
    mytable.operate('d')
    mytable.all_student()



