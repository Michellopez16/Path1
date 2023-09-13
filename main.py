print("Inicio de main")

#import operaciones as op
from operaciones import suma,resta,mensaje,saluda


"""
print(op.suma(1,2))
print(op.resta(1,2))

print(op.tmp)

op.mensaje = "hola 2"
print("Mensaje desde main.py:",op.mensaje)


"""

print(suma(1,1))
print(resta(1,1))

print(saluda())

print("-"*20)
print("var mensaje:",mensaje)
print("main:->",mensaje := "hola 2")
print("var mensaje:",mensaje)
print("-"*20)

print(saluda())

print("fin de main")    