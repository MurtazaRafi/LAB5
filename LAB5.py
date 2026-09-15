## Part of the lesson

# total = 100
# counter = 1
# def add_tax():
#     counter = counter
#     global total
#     total = total * 1.25
#     return counter

# print(add_tax())

## The lab 
# LAB 5
# Part A - Scope 
# 1.

course_name = "Python"

def my_courses():
    course_name = "C#"
    print("I love", course_name)

my_courses()
print("I don't like", course_name)

# "C#" is in a local scope (doesnt affect "Python")

# 2.

def count():
    counter = 0
# counter - unavailable

# 3.

# total = 100
# def add_tax():
#     total = total * 1.25
#     return total
# print(add_tax())

# The problem is total after the equal sign is not defined in that local scope
# Fix
total = 100
def add_tax(total):
    total = total * 1.25
    return total
print(add_tax(total))
# 4.
def func1():
    variabel1 = "var 1"
    def func2():
        variabel2 = "var 2"
        print(variabel1) #2
        print(variabel2) #3
    print(variabel1) #1
    func2()
func1()
# 1) func1 körs 2) func 2 körs

# 5
# def list(lst):
#     print(lst)

# list([1,2,3])

# part B - *args
# 1.
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add_all(1,2,3)) 

# 2.
def average(*numbers):
    if numbers is None:
        return 0
    return sum(numbers) / len(numbers)
print(average(1,2,3))

# 3.
def get_longest_word(*words):
    longest_word = ""
    length = 0 
    for word in words:
        if len(word) >= length:
            length = len(word)
            longest_word = word

    return longest_word
print(get_longest_word("Hej", "Hallå"))

# 4. 
def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence += word + separator
    return sentence

result = build_sentence("-", "Hej", "jag", "heter", "abcd")
print(result)

# 5. 
def describe_Score(student_name, *scores):
    total = 0
    count = 0

    for score in scores:
        total += score
        count += 1    
    return student_name, count, total/count

res = describe_Score("Murtaza", 100, 80, 70, 40)
print(res)

# part C - Positional unpacking
# 1. 

def three_parameter_function(*args):
    data1, data2, data3 = args
    print(data1)
    print(data2)
    print(data3)

lst = [10, 20, 30]
three_parameter_function(*lst)

# 2.
first_name = "Murtaza"
last_name = "Rafi"
city = "Stockholm"
tuple = (first_name, last_name, city)
def introduce(*tuple):
    for element in tuple:
        print(element, "-")
introduce(*tuple) # OBS *tuple och ej bara tuple

# 3
