happy = True
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")

hours = input ('Enter number of hours you worked this week:')
hours = int(hours)
normal_rate = 51.54
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate

print (f' This weekly payment is :{pay}')

numbers = [3,9,1,5,7,2,11,0,3,12,15]

temp_largest = numbers [0]
print('Before',temp_largest)

for number in numbers :
    if number > temp_largest :
        temp_largest = number
    print(number, temp_largest)

print (f'The largest value is {temp_largest}')


for i in range(1,4):
    for j in range(1,4):
        if i <= j:
         print (i,j)

for even in range(0, 10, 2):
    if even > 2:
        continue
print(even)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
nof_suburbs = []
for n in f_suburbs:
    if n[0] == 'F':
        nof_suburbs.append(n)
for suburb in nof_suburbs:
    f_suburbs.remove (suburb)