peso=float(input("¿Cual es tu peso en KG?: "))

altura=float(input("¿Cual es tu altura?"))

imc= peso/(altura * altura)

print(f"Su imc es de {imc}")

if imc < 18.5:
    print("Por debajo de lo normal")
elif imc <= 25:
    print("Tu peso es normal")
else:
    print("Por encima de lo normal")
