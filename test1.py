# print("Hello ward")

# def funkcja():

#     print("Ala")
#     a = 5
#     imie = "zbyszek"

# a = 5
# print(type(a))

# imie = "Ala"
# imie = 'Ala'
# imie = """Ala
# ma
# kota"""
# print(type(imie))
# imie = 5
# print(type(imie))
# imie = 4.3
# print(type(imie))
# def funkcje():
#     """docstring"""
#     pass

# liczba = int(5)
# liczba = int("5.5")
# print(liczba)

imie = "ala"
imie.capitalize()

print(imie)
print(imie[0])
print(imie.capitalize())
# imie[0] = "b" - nei zadziała

print("ala".capitalize().count('a'))    
print(imie + imie)   
# print(5 + imie)  
print("{} ma {} lat")
# print(imie + " ma" +5+ "lat") - nie dziala
print(imie + " ma" +str(5)+ "lat")
print("{} ma {} lat".format(imie, 5))
print("{1} ma {0} lat".format(imie, 5))
wiek = 1
print(f"{imie} ma {wiek} lat")


lista = []
lista = [1,3,'xd', 4.5, imie, [1,2]]
lista[0]
print(lista[5][1])

lista2 = lista + lista
print(lista2)

slownik = {}
slownik = {'imie': 'marek', 'wiek':35}
print(slownik.keys())
print(slownik.values())
print(slownik.items())

from math import *
import math as m
from math import pow as m_pow

pow()
m.pow()


