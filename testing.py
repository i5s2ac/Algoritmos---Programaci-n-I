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
from Recursion.Factorial_of_n  import factorial
from Recursion.Countdown import cuenta_atras

import Sorting
from Sorting.bubble_sort import bubble_sort
from Sorting.selection_sort import selection_sort
from Sorting.bubble_sort_optimized import bubble_sort_optimized


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

print("---------------------------| ALGORITHM # 7: FACTORIAL OF N |--------------------------------------- ")
print("")

print("El factorial es:",factorial(5))

print("")

print("---------------------------| ALGORITHM # 8: COUNTDOWN |------------------------------------------- ")
print("")

print(cuenta_atras(5))

print("")

print("---------------------------| ALGORITHM # 9: BUBBLE SORT |-------------------------------------------")
print("")

lista=[-2,45,0,11,-9]
print("Lista desordenada: ", lista)
sorted_list=bubble_sort(lista)
print("Lista ordenada: ",sorted_list)

print("")

arr = [9, 5, 4, 7, 10, 14, 15, 13, 8, 2]
arr2 = [8, 5, 7, 8, 9, 10, 5 ,7, 3, 2]

print("---------------------------| ALGORITHM # 10: SELECTION SORT |---------------------------------------")
print("")

print(selection_sort(arr))

print("")

print("---------------------------| ALGORITHM # 11: BUBBLE SORT OPTIMIZED  |-------------------------------")
print("")

print(bubble_sort_optimized(arr))

print("")