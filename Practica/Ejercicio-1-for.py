contmayorzero = 0
contzero = 0
contmenorzero = 0
for i in range(5):
    num = int(input("Ingrese un numero: "))
    if num < 0:
        contmenorzero += 1
    elif num > 0:
        contmayorzero += 1
    else:
        contzero +=1

print(f"\nMayores a 0 = {contmayorzero}\nMenores a 0 = {contmenorzero}\nIguales a 0 = {contzero}\n")