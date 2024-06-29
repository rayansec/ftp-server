import socket

if __name__ == "__main__":
    # defining the socket parameters
    host = "127.0.0.1"
    port = 8080
    totalClients = int(input("Enter number of client: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(totalClients)
    connections = []
    print("Initialing clients")

    #LOOP
    for i in range(totalClients):
        conn = sock.accept()
        connections.append(conn)
        print("connected with client", i+1)

    fileno = 0
    idx = 0
    for conn in connections:
        idx += 1
        data = conn[0].recv(1024).decode()
        if not data:
            continue
        filename = "output"+str(fileno)+".txt"
        fileno = fileno + 1
        fo = open(filename, "w")
        while data:
            if not data:
                break
            else:
                fo.write(data)
                data = conn[0].recv(1024).decode()
        print()
        print("Receiving file from Client", idx)
        print()
        print("Received successfully! New filename is: ", filename)
        fo.close()
    # closing connection
    for conn in connections:
        conn[0].close()


