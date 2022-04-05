import time, socket, sys

def startServer():
    new_socket = socket.socket()
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)

    port = 8080

    new_socket.bind((host_name, port))
    print( "Binding successful!")
    print("This is your IP: ", s_ip)

    name = input('Enter name: ')

    new_socket.listen(1)


    while True:
        conn, add = new_socket.accept()

        print("Received connection from ", add[0])
        print('Connection Established. Connected From: ',add[0])

        clientListen(conn, add, name)

    new_socket.close()
    print("Server has stopped")

def clientListen(conn, add, name):
    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')

    conn.send(name.encode())
    while True:
        message = input('Me : ')
        conn.send(message.encode())
        try:
            message = conn.recv(1024)
            message = message.decode()
            print(client, ':', message)
        except ConnectionError:
            break
    print(f"{add} has stopped")

startServer()

