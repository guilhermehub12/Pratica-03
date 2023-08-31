import socket, sys

def server(name):
    server_address = ('', 5004)
    # Create the datagram socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_address)
    s.listen(1)

    print(f"Olá {name}, o servidor está aguardando conexão...")
    conn, addr = s.accept()

    message = ""

    data = conn.recv(1024)
    peer_name = data.decode('utf-8')
    conn.sendall(name.encode('utf-8'))

    while message != "fim":
        data = conn.recv(1024)
        print(f"{name} recebeu mensagem de {peer_name}: ", data.decode('utf-8'))
        if not data:
            conn.sendall(data)
        message = input(f'{name}, digite uma mensagem: ')
        conn.sendall(str.encode(message))

    conn.close()
    s.close()

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

def main(peer_type, user_name):
    if peer_type == 'server':
        server(user_name)
    if peer_type == "client":
        client(user_name)


if __name__ == '__main__':
    peer_type = sys.argv[1]
    user_name = sys.argv[2]

    main(peer_type, user_name)