# Universidad del Valle de Guatemala
# Lógica Matemática - Sección 20
# Grupo: Stack

# Autores:
#   Morales, María José     Carné: 19145
#   Gudiel, Alejandra       Carné: 19232
#   Álvarez, Diego          Carné: 19498
#   España, Martín          Carné: 19258
#   Pineda, Juan Pablo      Carné: 19087

# Lector de fórmulas booleanas en forma de cláusula
# Versión: 1.0

# Dependencies
from random import random
import bf as bf
import dpll as dpll

# Shows information banner
print("###########################################")
print("Universidad del Valle de Guatemala")
print("Lógica Matemática - Sección 20")
print("\nAutores: \n\nAlejandra Gudiel      Carné: 19232 \nDiego Álvarez         Carné: 19498")
print("Juan Pablo Pineda     Carné: 19087 \nMaría José Morales    Carné: 19145 \nMartín España         Carné: 19258 \n")
print("Bienvenido al lector de fórmulas booleanas.")
print("###########################################")


# Program's status flag
active = True

# Main loop
while active:
    # Get user's input
    print("\no-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o")
    menuChoice = input("Menú de opciones: \n1. Ingresar Fórmula (Algoritmo Fuerza Bruta)\n2. Ingresar Fórmula (Algoritmo DPLL) \n3. Salir del programa \n\nIngrese una opción: ")
    print("o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o \n")

    # Algoritmo de fuerza bruta
    if menuChoice == '1':
        print("Opción 1")
        bf.brute_force()
    
    # Algoritmo DPLL
    elif menuChoice == '2':
        print("Opción 2")
        dpll.dpll()
    
    # Exit the main loop and therefore the program
    elif menuChoice == '3':
        print("**************************************************")
        print("¡Gracias por utilizar el programa! ¡Vuelva pronto!")
        print("************************************************** \n")

        active = False

    # Bulletproof
    else:
        print("****************************************************")
        print("INPUT ERROR: Por favor, ingrese una opción válida.")
        print("****************************************************")
