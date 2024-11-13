import socket

# Endereço IP e porta do servidor
host = '26.9.174.145'  # substitua por seu IP público
porta = 8080

# Criar socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind do socket à porta
sock.bind((host, porta))

# Escutar conexões
sock.listen(1)
print(f"Aguardando conexão em {host}:{porta}")

# Aceitar conexão
conn, addr = sock.accept()
print(f"Conexão estabelecida com {addr}")

# Receber mensagem
mensagem = conn.recv(1024)
print(f"Mensagem recebida: {mensagem.decode()}")

# Fechar conexão
conn.close()
sock.close()

