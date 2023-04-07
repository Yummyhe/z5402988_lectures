str = '''John said: "Let's learn Python together."'''
print(str)

f = 0.2 + 0.2 + 0.2
print(f == 0.6)
print(f)

i = 1
test = i = 1
print(test)

print("1"+"1"+"1")
print("2"*2)

y='abc'.upper()
print(y)

l = 56
w = 33
h = 30.5
v = l * w * h
print(f"the volume of the box is {v} cubic centimenters")

lst = [1, 2, 3]
print(lst)
t = type(lst)
print(t)

lst = [1, "string", True, None]
print(lst[2])
print(lst[-2])

lst = ["a", "b", "c", "d", "e", "f"]
print(f"The slice from index 1 through 4 is {lst[1:4]}" )

lst = [1, True, None]
lst.insert(1, "string")
print(f"After insertion, lst is now {lst}")

lst = ["from" , "firstname.surname",  "@" , "unsw.edu.au" , "Tue Oct 06 10:10:15 2020"]
print(f"The domain name is {lst[3]}")

line = "from firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020"
domain = line.split()[1].split('@')[1]
print(domain)
