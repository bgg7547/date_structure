class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = "男"

    def study(self):
        self.sex = "女"
        print("%s学习"%(self.name))

    def xiuxi(self):
        print("休息")
s1 = Student("zs",12)
s1.study()
print(s1.age)
print(s1.sex)