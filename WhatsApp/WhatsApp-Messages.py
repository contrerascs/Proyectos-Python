import pywhatkit

#Ingresar numero manualmente para no mostrarlo en código
numero_telefono = input("Ingresa numero de telefono: ")

#Parametros "23","30" son la hora en la que se enviará el mensaje
pywhatkit.sendwhatmsg("+52"+numero_telefono,"Test",23,30, 15, True, 2)