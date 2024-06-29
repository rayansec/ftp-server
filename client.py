import socket

if __name__ == "__main__":
    # defining the socket parameters
    host = "127.0.0.1"
    port = 8080
    totalClients = int(input("Enter number of client: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(host, port)

    # file transfer loop
    while True:
        filename = input("Input filename you want to send/transfer: ")
        try:
            fi = open(filename, "r")
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = fi.read()
            fi.close()
        except IOError:
            print("Your input invalid filename! Please try again...")