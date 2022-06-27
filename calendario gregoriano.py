año = int(input("Introduzca un año:"))
if año<1582:
    print ("No dentro del calendario Gregoriano")
else:
    if año%4==0 :
       print ("Año Bisiesto")
    elif año%100==0:
       print ("Año Bisiesto")
    else:
       print ("Año Comun")
#
# Coloca tu código aquí.
#
