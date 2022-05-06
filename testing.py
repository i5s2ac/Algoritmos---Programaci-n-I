import Listas
from Listas.largest_number_in_list import find_max
from Listas.list_merge import merge

import brute_force
from brute_force.sum_of_first_n_numbers import sum_first_numbers
from brute_force.pin_unlock import unlock

import Recursion
import sys
sys.setrecursionlimit(2000)
from Recursion.sum_of_first_n_numbers_recursive import sum_of_n
from Recursion.Nth_fibonacci_number import fibonacci_sequence

print("----------------------------| ALGORITHM # 1: LARGEST NUMBER IN A LIST |----------------------------  ")
print("")

arr=[2, 5, 1, 7, 10]
find_max(arr)
print("El número más grande en la lista es: ",find_max(arr))

print("")

print("----------------------------| ALGORITHM # 2: LIST MERGE |------------------------------------------- ")
print("")

lista1=[1,4,9]
lista2=[2,3,8]
merge(lista1, lista2)

print("")

print("---------------------------| ALGORITHM # 3: SUM OF FIRST N NUMBERS |-------------------------------- ")
print("")

n=input("Ingrese un número natural: ")
n=int(n)
print("Numero ingresado: ",n)
sum_first_numbers(n)

print("")

print("---------------------------| ALGORITHM # 4: 4-DIGIT PIN UNLOCK |----------------------------------- ")
print("")

print(unlock("2412"))

print("")

print("---------------------------| ALGORITHM # 5: SUM OF FIRST N NUMBERS (RECURSION) |------------------- ")
print("")

print("Sum of n:",sum_of_n(1000))

print("")

print("---------------------------| ALGORITHM # 6: NTH FIBONACCI NUMBER |--------------------------------- ")
print("")

print("Fibonacci Number:",fibonacci_sequence(32))

print("")