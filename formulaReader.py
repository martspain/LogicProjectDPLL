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
import itertools

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
        exp = input("Ingrese una expresion cnf en este formato [{(p, False), (q, False)}, {(p, True), (r, True)}]:\n")
        lista = []
         

        def array(exp):
            a = exp.replace("[",'')
            b = a.replace("]", '')
            c = b.replace("{",'')
            d = c.replace("(",'') 

            s1 = d.split("}, ")
            for d in s1:
                d1 = d.replace("), ","+")
                d2 = d1.replace(")","+")
                e = d2.split('+')
                del e[-1]
                literal = []
                for l in e:
                    v = l.split(", ")
                    if(v[1] == 'False'):
                        v[1] = False
                    else:
                        v[1] = True
                    literal.append(v) 
                lista.append(literal)
            return lista

        w = array(exp)

        def brute_force(cnf):
            literals = set()
            for conj in cnf:
                for disj in conj:
                    literals.add(disj[0])
         
            literals = list(literals) 
            n = len(literals)
            for seq in itertools.product([True,False], repeat=n):
                a = zip(literals, seq)
                #if all([bool(disj.intersection(a)) for disj in cnf]):
                intersection = []
                for cong in cnf:
                    for disj in cong:
                        for asg in a:
                            if set(asg) == set(disj):
                                intersection.append(asg)
                if len(intersection) == 0:
                    return False, None
                else:
                    cont = 0
                    r = []
                    while (cont < len(literals)):
                       r.append(str(literals[cont]) +" = " + str(seq[cont]))
                       cont = cont +1
                    return True, r

        print(brute_force(w))
        print("Opción 1")
    
    # Algoritmo DPLL
    elif menuChoice == '2':
        print("Opción 2")
    
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
