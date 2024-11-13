import socket

# Endereço IP e porta do servidor
host = '192.168.56.1'  # substitua pelo IP público ou local do servidor
porta = 8080

# Criar socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar ao servidor
    sock.connect((host, porta))
    
    # Enviar mensagem
    mensagem = input("Digite a mensagem: ")
    sock.sendall(mensagem.encode())
    
finally:
    # Fechar conexão
    sock.close()
