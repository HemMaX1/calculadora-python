def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b 

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede divir entre 0"
    return a / b

print("===calculadora pro===")
print("Operaciones: + - * /")


num1 = float(input("Primer numero"))
num2 = float(input("segundo numero"))
operacion = input("elige operaciones:")

if operacion == "+":
    resultado = sumar(num1,num2)
elif operacion == "-":
    resultado = restar(num1, num2)
elif operacion == "*":
    resultado = multiplicar(num1,num2)
elif operacion == "/":
    resultado = dividir(num1, num2)
else:
    resultado = "operacion no valida"

print("Resultado:{resultado}")   