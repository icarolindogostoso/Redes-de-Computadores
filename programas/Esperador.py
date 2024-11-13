import socket
# socket seria uma comunicacao entre maquinas


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.socket() -> cria um novo socket
                                                            # socket.AF_INET -> indica que o socket usará o protocolo IPv4
                                                            # socket.SOCK_DGRAM -> indica que o tipo de socket será UDP, isto é, um protocolo de comunicação não orientado à 
                                                                                 # conexão, permitindo envio de mensagens sem garantir a entrega.

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # sock.setsockopt() -> abre as configurações do socket
                                                                # socket.SOL_SOCKET -> indica que a opção a ser configurada vai ser a nivel de socket
                                                                # socket.SO_BROADCAST -> indica que vai configurar o broadcast -> vai ligar (1)

    sock.bind(("0.0.0.0", 5005))    # sock.bind() -> associa o socket a um endereço de IP, deixando aberto para receber dados
                                    # "0.0.0.0" -> este endereço IP especial indica que o socket deve escutar em todas as interfaces de rede disponíveis no dispositivo
                                    # 5005 -> porta onde o socket estará escutando

    while True:
        data, addr = sock.recvfrom(1024)    # sock.recvfrom() -> esta função bloqueia até que uma mensagem seja recebida
                                            # 1024 ->  tamanho máximo dos dados que podem ser recebidos de uma só vez (em bytes)
                                            # data -> a variável que armazenará os dados recebidos
                                            # addr -> a variável que armazenará o endereço do remetente (IP e porta) de onde a mensagem foi enviada
        print(data, " recebido de", addr)
except KeyboardInterrupt:
    print("Fechando...")