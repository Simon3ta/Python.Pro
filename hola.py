import random
contrasena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("intoduce la longitud:"))

termin = ''.join(random.choice(contrasena) 
for i in range(longitud))
print("la contraseña generada es:",termin) 