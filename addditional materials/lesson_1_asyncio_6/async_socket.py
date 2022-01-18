import asyncio
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 7777))
server_socket.listen()
# server_socket.setblocking(False)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setblocking(False)


async def server_work():
    client, address = await server_socket.accept()
    msg = await client.recv(1024)
    print('msg from client_dist: ', msg.decode('utf-8'))
    client.send('Hi, client_dist!'.encode('utf-8'))
    client.close()


async def client_work():
    client_socket.connect(('127.0.0.1', 7777))
    client_socket.send('Hi, server_dist'.encode('utf-8'))
    msg = await client_socket.recv(1024)
    print('msg from server_dist: ', msg.decode('utf-8'))
    client_socket.close()


async def main():
    task1 = asyncio.create_task(server_work())
    task2 = asyncio.create_task(client_work())
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(main())
