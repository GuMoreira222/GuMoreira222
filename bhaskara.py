from math import sqrt 

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b*b - 4 * a * c

x1 = (-(b) + sqrt(d))/2*a

x2 = (-(b) - sqrt(d))/2*a

print (f"A primeira resposta é {x1}\n")
print (f"A segunda resposta é {x2}\n")