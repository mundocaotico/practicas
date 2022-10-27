import datetime
fecha = datetime.datetime.now()
#dia = fecha.strftime("%x").replace(" ","").replace(":","").replace("/","")
#hora = fecha.strftime("%X").replace(":","")

#mensaje = print(dia.strip(),"-",hora.strip())
nombre_fichero = (fecha.strftime("%x%X").strip().replace("/","").replace(":",""))
print("netplan-{nombre_fichero}".format(nombre_fichero = nombre_fichero))
#file = open("netplan{mensaje}".format(mensaje = mensaje), "w")

print("Bienvenido al generador de Netplan")
print("Para generar el archivo netplan, es necesaria la sigiente informacion")
print("1: Nombre de la interfaz,",
 "\n2: Se va a utilizar DHCP?",
 "\n3: En caso negativo: Dirección IP local, mascara de red, gateway, y servidores DNS")

dhcp = input("Se va a utilizar DHCP? (S/N): ")
if (dhcp == "N"): 
    interfaz = input("Introduce el nombre de la interfaz de red: ")
    ip = input("Introduce la direccion IP que va a tener el equipo: ")
    mascara = input("Introduce la mascara de red en formato CIDR (/24): ")
    gateway = input("Introduce la direccion de la puerta de enlace: ")
    dns = input("Introduce uno o dos DNS (separados por coma, de ser dos): ")

    print("GENERANDO LINEAS DEL FICHERO")
    print("\n")

    print("network:",
    "\n  ethernets:",
    "\n    {interfaz}:".format(interfaz = interfaz),
    "\n      dhcp4: false",
    "\n      addresses: [{ip}{mascara}]".format(ip = ip, mascara = mascara),
    "\n      gateway4: {gateway}".format(gateway = gateway),
    "\n      nameservers:",
    "\n        addresses: [{dns}]".format(dns = dns),
    "\n  version: 2"
    )

else:
    print("MODO CONFIGURACION AUTOMATICA")
    interfaz = str(input("Introduce el nombre de la interfaz de red: "))
    print("GENERANDO LINEAS DEL FICHERO")
    print("\n")

    print("network:",
    "\n  ethernets:",
    "\n    {interfaz}:".format(interfaz = interfaz),
    "\n      dhcp4: true",
    "\n  version: 2"
    )
    
