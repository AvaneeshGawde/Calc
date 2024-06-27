from bigLoad.add_sub import add
from bigLoad.add_sub import sub
from bigLoad.mul_div import mul
from bigLoad.mul_div import div
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
d = int(input("enter d"))

print(f"value of a: {a}")
print(f"value of b: {b}")
print(f"value of c: {c}")
print(f"value of d: {d}")

print()

print(f"Addition {add(a,b)}")
print(f"Subtraction {sub(a,b)}")
print(f"Multiplication {mul(c,d)}")
print(f"Division {div(c,d)}")