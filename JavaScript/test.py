print(False and "candy")

class Haeni:
    name = "Haeni"
    age = 24

HH = Haeni()

print(Haeni.name)
print(HH.name)

HH.name = "HH"
print(HH.name)
print(Haeni.name)

print('----------')

n_list = [1,2,3]

a = n_list
b = n_list.copy()

print(a)
print(b)

b.append(5)
a.append(4)

print(a)
print(b)
print(n_list)