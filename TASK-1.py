#task-1
userName = 'Vitaliy'
userAge = 23
user = [userName,userAge]
print (user)
frends = ['Vitiy','Zahar','Ernest', 'Slavik']
print(frends)

dict = {"Vitiy": "Developed", "Zahar": "Beatuful", "Ernest": "Sensai", "Slavik": "Stylish"}
for a in dict.items():
    print(a)

City = {"Krasnodar","Mihoz", "Spain", "Mihoz"}
print(City)

print(frends[1])

clock = int(input("How many hours are in dota 2?"))
if (clock <=100):
    print("Archon")
elif (clock >= 100) and (clock < 300):
    print("Crusader")
elif (clock >= 300) and (clock <1000):
    print("Guardian")
else:
    print("Herald")

c = 1
while c < 3:
    print("ok")
    c += 2


for frend in frends:
    print(frend)

a = 'TEST'
b = 'E'
if b in a:
    print('pass')

