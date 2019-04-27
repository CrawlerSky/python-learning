
'''
python类的学习！
'''

'''
实例属性和类属性：
在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
'''

# 创建一个员工类
class Employee(object):
    city = 'Nanjing China'; # 类属性

    '''
    如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加__name、__sex和__age属性。
    '''
    __slots__ = ('__name', '__sex', '__age') # 用tuple定义允许绑定的属性名称

    '''
    构造函数:__init__(self, ...)方法的第一个参数永远是self，表示创建的实例本身.
    如果要让内部属性不被外部访问，在属性的名称前加上两个下划线__,变成私有成员变量.
    '''
    def __init__(self, name, sex, age):  # 构造方法
        self.__name = name;  # 实例属性
        self.__sex = sex;
        self.__age = age;

    # 外部实例变量无法访问__name, __age等私有成员，
    # 可以通过暴露get()和set()方法使得外部代码能够获取和修改类的私有成员
    def get_name(self):
        return self.__name;
    def set_name(self, name):
        self.__name = name;
        
    '''
    普通方法：定义一个方法，除了第一个参数是self外，其他和普通函数一样。
    '''
    def print_info(self):
        print('%s -- %s -- %d' % (self.__name, self.__sex, self.__age));

    # 员工工作的方法
    def work(self, time):
        print('Employee: %s is working for %d hours!!!' % (self.__name, time));


'''
类的继承！！！
'''
class Teacher(Employee):
    # 构造函数
    def __init__(self, name, sex, age, salary):
        super(Teacher, self).__init__(name, sex, age); # 初始化父类
        self.salary = salary;

    def work(self, time):
        print('Teacher: %s is teaching for %d hours!!!' % (self.__name, time));


class Student(Employee):
    # 构造函数
    def __init__(self, score):
        self.score = score;

    def work(self):
        print('Student: %s gets %d points in test!!!' % (self.__name, self.score));        


'''
多态理解： 父类引用指向子类对象！
'''


employee = Employee('zengsk', 'nan', 24);
employee.print_info();
print(Employee.city);



tcher = Teacher('Wang', 'nan', 30, 10000);
tcher.print_info();
print(tcher.salary);






