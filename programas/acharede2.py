def mascara_inteiro(mascara):
    mascara_ret = [0,0,0,0]
    for i in range(4):
        if mascara >= 8:
            mascara_ret[i] = 255
            mascara = mascara - 8
        else:
            mascara_ret[i] = 255 - (2**(8 - mascara) - 1)
            mascara = 0
    return mascara_ret
    
def aplicacao (ip, mascara):
    rede = 0
    for i in range(4,0,-1):
        oc = ip[i] * mascara[i] // 255
        rede = rede + oc * (256**(i-1))
    return rede

def broadcast (ip, mascara):
    complemento = []
    for i in range(4):
        complemento[i] = 255 - mascara[i]
        
    broadcast_lista = []
    for i in range(4):
        soma = ip[i] + mascara[i]
        if soma > 255:
            soma = 255
        broadcast_lista[i] = soma
        
    broadcast = 0
    for i in range(4):
        broadcast = broadcast + (broadcast_lista[i] * (255**(3-i))) 
        
    return broadcast

ip1 = input()
ip2 = input()
mascara = int(input())

ip1_lista = ip1.split(".")
ip2_lista = ip2.split(".")
mascara_lista = mascara_inteiro(mascara)
broadcast_lista = broadcast(ip1_lista, mascara)

rede1 = aplicacao(ip1_lista, mascara_lista)
rede2 = aplicacao(ip2_lista, mascara_lista)

if rede1 == rede2:
        print("\nOs IPs estão na mesma rede.")
    else:
        print("\nOs IPs não estão na mesma rede.")
