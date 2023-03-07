# solution for tasks two
cloak = input()
print(cloak)

print(f'Сколько времени?{cloak}')

with open('text.txt', 'w') as f:
    print(f.write('hello_world'))
def calculator (a,b):
    return (a+b)
print(calculator(1, 3))

def total (*numbers):
    print(1,2,32,412,412,532,)
print(total())


x = 1
def number ():
    global x
    x = 5
    print(x)
number()

