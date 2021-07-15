class Person(object):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def walk(self):
        print(f"{self.name} is walking...")

    def __str__(self):
        return self.name



class Student(Person):

    def __init__(self, name,sex, score):
        super().__init__(name,sex)
        self.score = score
        
    def learning(self):
        print(f"{self.name} is learning...")

    def __str__(self):
        return f"{self.name}, {self.score}"


st = Student('zz','男', 100)

print(st)
print(st.sex)
st.learning()
st.walk()