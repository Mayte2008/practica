ingreso=float(input("Ingrese el ingreso anual:"))
if ingreso<85528:
   impuesto=ingreso*0.18-556.02
   impuesto=round(impuesto, 0)
   print ("Debe pagar: ",impuesto , "pesos")
else:
   impuesto=(ingreso-85528)*0.32 +14839.02
   impuesto=round(impuesto, 0)
   print("Debe pagar: ",impuesto )

