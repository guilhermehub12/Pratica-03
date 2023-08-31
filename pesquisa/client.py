import socket, sys

def client(name):
    server_address = ('127.0.0.1', 5004)
    message = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_address)

    s.sendall(name.encode('utf-8'))
    data = s.recv(1024)
    peer_name = data.decode('utf-8')


    while message != "fim":
        message = input(f'{name}, digite uma mensagem: ')
        s.sendall(message.encode('utf-8'))

        data = s.recv(1024)
        print(f'{name} recebeu mensagem de {peer_name}: ', data.decode('utf-8'))
    s.close()

if __name__ == '__main__':
    user_name = sys.argv[1]
    client(user_name)