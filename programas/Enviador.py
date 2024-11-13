import socket
import sys

def main():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), 
                                    port=None, 
                                    family=socket.AF_INET)  # socket.getaddrinfo() -> esta função retorna uma lista de tuplas com informações sobre os 
                                                            # endereços de rede disponíveis para o host especificado

                                                            # host = socket.gethostname() -> Esta função retorna uma lista de tuplas com informações sobre 
                                                            # os endereços de rede disponíveis para o host especificado. Isso indica que você está buscando 
                                                            # informações sobre as interfaces do próprio dispositivo.

                                                            # port=None -> você não está filtrando as informações por uma porta específica. Você receberá 
                                                            # informações sobre todas as interfaces disponíveis, independentemente da porta.

                                                            # family=socket.AF_INET -> você está interessado apenas nas interfaces que utilizam o protocolo
                                                            # IPv4

                                                        
    print(interfaces) # interfaces = [(<AddressFamily.AF_INET: 2>, 0, 0, '', ('26.9.174.145', 0)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('192.168.0.175', 0))]
    
    allips = [ip[-1][0] for ip in interfaces]   # A lista resultante allips conterá todos os endereços IP disponíveis na máquina, extraídos das informações 
                                                # de interfaces. Cada endereço será uma string representando um endereço IPv4.

    print(allips) # ['26.9.174.145', '192.168.0.175']

    msg = str.encode(sys.argv[1]) if len(sys.argv) > 1 else b'Teste'    # sys.argv -> É uma lista em Python que contém os argumentos da linha de comando
                                                                        # passados para o script quando ele é executado. O primeiro elemento (sys.argv[0])
                                                                        # é sempre o nome do próprio script, e os elementos subsequentes são os argumentos
                                                                        # fornecidos pelo usuário.

                                                                        # A variável msg conterá a mensagem que será enviada. Se o usuário fornecer um 
                                                                        # argumento ao executar o script, msg será esse argumento convertido para bytes. 
                                                                        # Se não houver argumento, msg será a string 'Teste' já convertida para bytes.

    print(msg)  # b'isto eh uma mensagem'

    for ip in allips:
        print(f'Enviando para {ip}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # socket.IPPROTO_UDP -> Especifica o protocolo a ser utilizado (UDP), 
                                                                                    # embora seja opcional já que o tipo de socket SOCK_DGRAM já indica isso.

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.bind((ip,0))

        sock.sendto(msg, ("255.255.255.255", 5005)) # sock.sendto() -> Envia a mensagem (msg) para o endereço de broadcast 255.255.255.255 na porta 5005.
                                                    # "255.255.255.255" -> Este é o endereço de broadcast que envia a mensagem para todos os dispositivos
                                                    #  na rede local.

        sock.close()


main()