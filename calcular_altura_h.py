# input 
h =int(input("Digite numero  de rebotes: "))

# processing 
q = h / 5
n = 0 
while h>=q:
    h = h - 0.1 *h 
    n = n + 1
print("el 5to rebote de la pelota tendra una altura de:  " + str(n))