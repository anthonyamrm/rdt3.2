import socket
import pickle
import hashlib

##num_seq_global = 0

PORT = 5556
SERVER = "" #Colocar o IP do server
ADDR = (socket.gethostbyname(socket.gethostname()), PORT)
DESTINO_SERVER = (SERVER, 5555)
TIME_WAIT = 3

desconectar = "disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def calculo_checksum(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def fazer_pacote(num_seq, msg, destino):
    pacote = (num_seq, msg, calculo_checksum(msg), destino)
    return pacote

def enviar(msg, destino):
    num_seq = 0
    pacote = fazer_pacote(num_seq, msg, destino)
    pkg = pickle.dumps(pacote)
    server.sendto(pkg, DESTINO_SERVER)
    ##num_seq_global = 1 - num_seq_global
    pacote, destino_server = server.recvfrom(1024)
    pacote = pickle.loads(pacote)
    num_seq, msg, checksum, destino_sender = pacote
    print(msg)
    
    
if __name__ == '__main__':
    print("Você está conectado ao server")
    ip_dest_receiver = input("Digite o endereco IP do destino: ")
    gate_dest_receiver = int(input("Digite a porta do destino: "))
    mensagem = "_"
    while mensagem != desconectar:
        message = input("Digite a mensagem que você quer enviar: ")
        destino = (ip_dest_receiver, int(gate_dest_receiver))
        enviar(message, destino)