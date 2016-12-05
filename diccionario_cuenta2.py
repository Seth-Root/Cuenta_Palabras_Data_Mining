# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

from collections import Counter

from prettytable import PrettyTable

import matplotlib.pyplot as plt

import numpy as np 

cadena = raw_input("Escriba una cadena de caracteres: ")

diccionario_clave_valor = dict()

for caracter in cadena:
    if caracter not in diccionario_clave_valor:
        diccionario_clave_valor[caracter] = 1
    else:
        diccionario_clave_valor[caracter] = diccionario_clave_valor[caracter] + 1
print diccionario_clave_valor



#listas_para_pretitable 

listas_clave = []
listas_valor = []

# Recorrer un diccionario, imprimiendo su clave-valor
for clave,valor in diccionario_clave_valor.items():
    listas_clave.append(clave)
    listas_valor.append(valor)

print listas_valor
print listas_clave


num_listas_valor = len(listas_valor)
table = PrettyTable(["          Valor      ", "       Clave    "])
for i in range(0,num_listas_valor):
    
    table.add_row([listas_valor[i], listas_clave[i]])
    i += 1

print table

posicion_y = np.arange(len(listas_clave))
plt.barh(posicion_y, listas_valor, align = "center")
plt.yticks(posicion_y, listas_clave)
plt.xlabel('Numero de Repeticiones de los caracteres')
plt.title("Numero de Repeticiones")
plt.show()


explode = [0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0, 0, 0, 0, 0, 0.]

plt.pie(lista_nueva2, explode=explode, labels=listas_clave, autopct='%1.1f%%', shadow=True)
plt.title("Histograma de Clave Valor para Cadenas", bbox={"facecolor":"0.8", "pad":5}) 
plt.legend()
plt.show()













