#exercise 1
def my_function(fname):
    print(fname+ "shanmukh")
    
my_function("Email")
my_function("linus")

#exercise 2
def func1(*number):
    for i in number:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#exercise 3
def calculation(x, y):
    a = x + y 
    b = x - y
    return a,b


res = calculation(40, 10)
print(res)


#exercise 4

def show_employee(name, amount=9000):
    print("Name:", name, "salary:", amount)

show_employee("Ben", 12000)
show_employee("Jessa")


#exercise 5
def printNumbers(a, b):

    def sumNumbers(a, b):
        return a + b

    add = sumNumbers(a, b)
    return add + 5

result = printNumbers(5, 10)
print(result)


#exercise 6

def printNumber(num):
    if num:
        return num + printNumber(num - 1)
    else:
        return 0

x = printNumber(10)
print(x)


#exercise 7
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

show_Student = display_student

show_Student("Emma", 26)


#exercise 8

print(list(range(4, 30, 2)))

#exercise 9
a = [4, 6, 8, 24, 12, 2]
print(max(a))