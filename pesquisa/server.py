# Cliente-Servidor e P2P

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

if __name__ == '__main__':
    user_name = sys.argv[1]
    server(user_name)