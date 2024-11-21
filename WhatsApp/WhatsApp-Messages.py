import pywhatkit

numero_telefono = input("Ingresa numero de telefono: ")

pywhatkit.sendwhatmsg("+52"+numero_telefono,"Test",23,30, 15, True, 2)