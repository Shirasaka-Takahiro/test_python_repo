'''
class SampleClass:
    sample class 

sample = SampleClass()

sample.name = "A"
sample2 = SampleClass()

sample2.name = "B"

print(sample.name)
print(sample2.name)


class User:
    def __init__(self, name):
        self.name = name
        print("コンストラクタが呼ばれました")

    def hello(self):
        print("Hello " + self.name)

user = User("Sample User")
py = User("python")

user.hello()
py.hello()
'''

'''
class SampleClass:
    def set_name(self, name):
        self.name = name
    
    def hello(self):
        print("hello, {0}".format(self.name))

sample = SampleClass()
sample2 = SampleClass()
sample.set_name("Python")
sample2.set_name("AI")
sample.hello()
sample2.hello()
'''

'''
class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)

class SuperUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def hello(self):
        print("SuperHello " + self.name)

        super().hello()

t = SuperUser("tani", 100)
t.hello()
'''

'''
class SampleClass:
    "class"

sample = SampleClass()

sample.name = "A"
sample2 = SampleClass()

sample2.name = "B"

print(sample.name)
print(sample2.name)

class User:
    def __init__(self, name):
        self.name = name
        print("コンストラクタが呼ばれました")

    def hello(self):
        print("Hello " + self.name)

user = User("Sample User")
py = User("python")

user.hello()
py.hello()

class SampleClass:
    def set_name(self, name):
        self.name = name
    
    def hello(self):
        print("hello, {0}".format(self.name))

sample = SampleClass()
sample2 = SampleClass()
sample.set_name("Python")
sample2.set_name("AI")
sample.hello()
sample2.hello()
'''

class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello {0}".format(self.name))

class SuperUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def hello(self):
        print("SuperHello + {0}".format(self.name))

        super().hello()

t = SuperUser("Tani", 100)
t.hello()