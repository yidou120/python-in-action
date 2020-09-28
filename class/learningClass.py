class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myMethod(self):
        print("my name is : " + self.name)

person = Person("小米",10)
person.myMethod()
person.name = "消灭"
person.myMethod()

class Student(Person):
    """
    不给类添加任何属性和方法的标志
    pass
    """
    def __init__(self,name,age,year):
        Person.__init__(self,name,age)
        self.year = year
    def printList(self):
        print("student name is : "+self.name+", age is : "+str(self.age) + ", year is : " + str(self.year))
student = Student("小法",20,1998)
student.printList()