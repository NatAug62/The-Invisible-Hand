"""General utility functions

Classes:
    name -- summary
Exceptions:
    name -- summary
Functions:
    name -- summary
Globals:
    name -- summary
"""

import socket

def openTCP(portNum):
    """Receive an incoming TCP connection

    Parameters
        portNum -- int, which port to listen for a connection on
    Returns
        socket -- client socket associated with the connection made
    """
    print(f"Listening for TCP connection on port {portNum} ...")

    # create an IPv4 TCP server socket and set it up to listen
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TODO - do we need this???
    serverSocket.bind(('0.0.0.0', portNum))
    serverSocket.listen()

    # listen for incoming connections and accept them
    clientSocket, address = serverSocket.accept()
    print("Connection established")

    # close the server socket and return the socket associated with the connection
    serverSocket.close()
    return clientSocket

def openUDP(portNum):
    """Create a UDP socket to listen for incoming data

    Parameters
        portNum -- int, which port to listen for data on
    Returns
        socket -- socket used to receive incoming data
    """
    print(f"Creating UDP socket on port {portNum} ...")

    # create the UDP socket and bind it to the port
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TODO - do we need this???
    serverSocket.bind(('0.0.0.0', portNum))

    # return the bound UDP socket
    return serverSocket