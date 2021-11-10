x = [[a*b+1 for b in range(2,6)] for a in range(3,9)]
print("x =", x)

sl = slice(1, 5, 2)
y = x[sl]
print("y =", y)

temp_z = x[slice(len(x)-3, len(x)-2)]
z = temp_z[0][slice(len(temp_z[0])-2, len(temp_z[0]))]
print("z =", z)

t = x[len(x)-2:: -4]
print("t =", t)

u = x[-2]
u = u[::len(u)-2]
print("u =",u)
