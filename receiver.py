import socket
import pickle

PORT = 5557
SERVER = "192.168.4.10"
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "disconnect"
num_seq_esperado = 0

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(ADDR)

def receber_msg(): 
    pacote, remetente = receiver.recvfrom(1024)
    pacote = pickle.loads(pacote)
    num_seq, msg, checksum, destino = pacote
    print(msg)

if __name__ == "__main__":
    message = "blablabla"
    while message != DISCONNECT_MESSAGE:
        receber_msg()
        message = input("Digite disconnect para desconectar.")
