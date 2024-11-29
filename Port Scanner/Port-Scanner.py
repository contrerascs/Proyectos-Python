import socket

ip = input("Ingrese la dirección IP a escanear: ")

for puerto in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto Abierto: " + str(puerto))
    else:
        print("Puero Cerrrado: "+str(puerto))