"""
Autheur : Antoine Langevin
Fichier pour tester les différentes functions dans le module lab_13_module.
"""
# pylint: disable=no-member
import lab_13_module as tables

print("*** STARTER PROGRAM ***")
tables.multiplication_table_hardcoded()
print("*---------------------*")
tables.multiplication_table(7)
print("*---------------------*")
tables.multiplication_table_limite(7, 12)
print("*---------------------*")
tables.multiplication_table_custom(7, 2, 5)
print("*---------------------*")
tables.multiplication_table_custom_ref(6, 4, 7)
print("*---------------------*")
tables.multiplication_table_custom_ref(6, end=6)
print("*---------------------*")
tables.multiplication_table_custom_ref(3, end=3, start=1)
print("*---------------------*")
tables.multiplication_table_custom_ref(7)
print("*** Fermeture du programme ***")
