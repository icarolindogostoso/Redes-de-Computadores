def mascara_inteiro (mascara):
    mascara_int = 0
    for i in range(4,0,-1):
        if mascara >= 8:
            mascara_int = mascara_int + 255 * 256 ** (i-1)
            mascara = mascara - 8
        else:
            mascara_int = mascara_int + 255 - (2**(8 - mascara) - 1)
            mascara = 0
    return mascara_int

def ip_inteiro (ip):
    lista_ip = ip.split(".")
    ip_int = 0
    for i in range(4):
        ip_int = ip_int + int(lista_ip[i]) * 256 ** (3-i)
    return ip_int

def checar (ip1, ip2, mascara):
    ip1_lista = ip1.split(".")
    ip2_lista = ip2.split(".")
    check = False
    for i in range(4):
        if not ip1_lista[i].isdigit() or not ip2_lista[i].isdigit():
            check = True
            break
        if 0 > int(ip1_lista[i]) > 255 or 0 > int(ip2_lista[i]) > 255:
            check = True
            break
    if 0 > mascara > 32:
        check = True
    return check
    

ip1 = input("Insira um enredeço IP no modelo xxx.xxx.xxx.xxx: ")
ip2 = input("Insira um enredeço IP no modelo xxx.xxx.xxx.xxx: ")
mascara = int(input("Insira uma mascara de rede (1 - 32): "))

check = checar(ip1, ip2, mascara)
if check:
    print("Valores invalidos")
else:
    ip1 = ip_inteiro(ip1)
    ip2 = ip_inteiro(ip2)
    mascara = mascara_inteiro(mascara)

    ip_rede = ip1 & mascara
    broadcast = ip1 | (~mascara & 0xFFFFFFFF)

    if ip_rede < ip2 < broadcast:
            print("os IPs estao na mesma rede.")
    else:
        print("os IPs nao estao na mesma rede.")
