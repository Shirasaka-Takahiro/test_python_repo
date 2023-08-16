'''
print("Hello, World")
name = "Tom"
print("My name is" + name)
age = 24
print("My name is " + name + "My age is " + str(age))

string_price = "10000"
price = 50000
total_price = int(string_price) + price
print(total_price)

li = []
li.append("python")
print(li)
li.append("php")
print(li)

profile = {"name": "tani", "email": "a@example.com"}
print(profile["name"])
profile["gender"] = "male"
print(profile["gender"])
'''

''''
for i in range(10):
    if i%2==0:
        print("{} is even.".format(i))
    else:
        print("{} is odd.".format(i))


score = 80
if score > 78:
    print("passed")
else:
    print("failed")

score = 80
if score == 100:
    print("good")
elif score > 85:
    print("passed")
else:
    print("failed")

for i in ["apple", "banana", "melon"]:
    print(i)

for i in range(10):
    print(i)
'''

'''
data = [20, 40, 60, 80]
for d in data:
    print(d)

sum_d = 0
for d in data:
    sum_d += d
print(sum_d)

sum_d = 0
for d in data:
    sum_d += d
else:
    print(sum_d)

for i in range(10):
    if i == 3:
        continue
    print(i)

for i in range(10):
    if i ==3:
        break
    print(i)
'''

'''
data = [1, 2, 3, 4, 5, "f"]
for x in data:
    if x == "f":
        print('found')
        break
else:
    print("not found")

for char in "hello":
    print(char)

for index, name in enumerate(["apple", "banana", "melon"]):
    print(index, name)

print(list(range(20)))

data = {"tani": 21, "kazu": 22, "python": 33}
for key, value in data.items():
    print("key: {} value: {}".format(key, value))

n = 0
while n < 10:
    print(n)
    n +=1

result = [x**2 for x in range(1,11)]
print(result)

result = []
for i in range(1,11):
    result.append(i**2)
print(result)
'''

'''
print("Input your name")
name = input()
print("Your name is "+name)
'''

'''
while True:
    print("Please input")
    i = input()
    print(i)
'''

'''
def hello():
    print("hello")
hello()

def lowercase_userscore():
    print("score")
lowercase_userscore()

def test():
    pass

def say_hello(name):
    print("hello "+ str(name))
say_hello("Yamada")

def adder(a, b):
    return a+b
value = adder(5,10)
print(value)

data = [1,2,3,4,5]
value = len(data)
print(value)
'''

'''
def func(a, b=5):
    print(a)
    print(b)
func(10,15)
func(3)

def sample(arg, arg_list=[]):
    arg_list = []
    arg_list.append(arg)
    print(arg_list)
sample('python')
sample('Python')
'''

'''
def add(x1):
    x2 = 10
    result = x1 + x2
    print(result)
add(5)
'''

'''
def add(x1,x2):
    result = x1 + x2
    return result

x1 = 5
x2 = 10
result= add(x1, x2)
print(result)

glb = 0
def func1():
    glb = 1

def func2():
    global glb
    glb = 5

print(glb)
func1()
print(glb)
func2()
print(glb)


var1 = 'グローバル変数'

def sample():
    var2 = 'ローカル変数'
    return (var1, var2)
print(sample())
'''

'''
var1 = 'グローバル'
def sample():
    global var1

    var1 = 'ローカルに変更されました'
sample()
print(var1)
'''

