#conversão para int

x = 2     #int
y = 2.8   #float 
z = '2'   #string

print(x, y, z)

x = int(2)     #int
y = int(2.8)   #valor será adequado ao tipo int, perdendo o decimal.
z = int('2')   #valor será adequado ao tipo int

print(x, y, z)

#conversão para float

a = 2.3     #float
b = 2       #int
c = '2.3'   #string
d = '2'     #string
print(a, b, c, d)

a = float(2.3)     #float
b = float(2)       #adequado para float
c = float('2.3')   #adequado para float
d = float('2')     #adequado para float

print(a, b, c, d)

#conversão para str

t= 's1' #str
r = 2   #int
z = 2.3 #float

print("A variavel t é do tipo: ", type(t))
print("A variavel r é do tipo: ", type(r))
print("A variavel z é do tipo: ", type(z))

t= str('s1') #str
r = str(2)   #transformado em str
z = str(2.3) #transformado em str

print("A variavel t é do tipo: ", type(t))
print("A variavel r é do tipo: ", type(r))
print("A variavel z é do tipo: ", type(z))
