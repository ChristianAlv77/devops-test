# program.py

#imports
from datetime import date

print('Hello, World!')
print('Programa inicial!')
sum = 1 + 2
print(sum)
sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
print(type(shuttle_landed_on_the_moon)) ## <class 'float'>
print("Today's date is: " + str(date.today()))# funcion de casteo de fecha

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")