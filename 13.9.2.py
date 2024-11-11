##
fecha=input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
dia=fecha[:fecha.find('/')]
mesaño=fecha[fecha.find('/')+1:]
mes=mesaño[:mesaño.find('/')]
año=mesaño[mesaño.find('/')+1:]
print("Día",dia)
print("Mes",mes)
print("Año",año)