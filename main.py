a = [1,2,3,5,6,8]
b = ['чётное' if i % 2 == 0 else 'нечётное' for i in a]
print(b)

g = ["Flith Bluth" if j % 15 == 0 else 'Flith' if j % 3 == 0 else "Bluth" if j % 5 == 0 else j for j in range(1, 100)]
print(g)

l = [1,11,10,9,87]

f = [i if i>=10 else "0"  for i in l]
print(f)

h = {1,2,34,45,56,99}
d = ['even' if i % 2 == 0 else 'odd' for i in h]
print(d)

string = ['aaa', 'hello', 'My name is', 'help me','pila']
m = [len(i) if len(i) < 5 else "5" for i in string]
print(m)


k = [-1,2,4,6,-10,-5]
n = [i if i >= 0 else "0" for i in k]
print(n)

x = [1,2,45,66,77,67,50,12,35,79,0,3,4,5,6]
y = [i ** 2 if i % 2 == 0 else i**3 for i in x]
print(y)

z = [20, 35,89,144,23,19]
c = ['High' if i > 50 else 'Low' if i < 20 else 'Medium' for i in z]
print(c)

