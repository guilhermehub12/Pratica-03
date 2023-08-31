import socket
import struct
import sys

# emissor (sender) client
def emissor(name):
  MULTICAST_GROUP = '224.3.29.71'
  MULTICAST_PORT = 5007
  msg = ""

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  ttl = struct.pack('b', 1)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

  sock.sendto(f"Olá, grupo multicast!".encode('utf-8'),
              (MULTICAST_GROUP, MULTICAST_PORT))
  
  while msg != "sair":
    msg = input(f'{name}, digite uma mensagem: ')
    sock.sendall(msg.encode('utf-8'))

    data = sock.recv(1024)
    print(f'{name} recebeu mensagem de {usuario}: ', data.decode('utf-8'))
  sock.close()

# receptor (receiver) server
def receptor(name):
  MULTICAST_GROUP = '224.3.29.71'
  MULTICAST_PORT = 5007

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(('', MULTICAST_PORT))

  group = socket.inet_aton(MULTICAST_GROUP)
  mreq = struct.pack('4sL', group, socket.INADDR_ANY)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

  while True:
    print("Receptor aguardando mensagem...")
    data, addr = sock.recvfrom(1024)
    print(f"Recebido de {addr}: {data.decode('utf-8')}")


def main(tipo, usuario):
    if tipo == 'receptor':
        receptor(usuario)
    if tipo == "emissor":
        emissor(usuario)


if __name__ == '__main__':
    tipo = sys.argv[1]
    usuario = sys.argv[2]

    main(tipo, usuario)