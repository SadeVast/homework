# solution for tasks two
cloak = input()
print(cloak)

print(f'Сколько времени?{cloak}')

with open('Test.txt') as f:
    print(f.read())
def calculator (a,b):
    return (a+b)
print(calculator(1, 3))

def total (*numbers, **dictionary):
    print(numbers)
    print(dictionary)


x = 1
def number ():
    global x
    x = 5
    print(x)
number()

if __name__=='__main__':
    total(555,666, sec_1=456, sec_2 = 789)
