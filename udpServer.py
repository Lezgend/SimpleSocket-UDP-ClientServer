import socket

# ============================================================================

# !!! Configuration !!!
localHostname     = socket.gethostname()
localIP           = socket.gethostbyname(localHostname)
localPort         = 10000
bufferSize        = 1024

msgFromServer     = "Hello UDP Client"
bytesToSend       = str.encode(msgFromServer)

# ============================================================================

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP Server UP and Listening")

# Listen for incoming datagrams
try:
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client: {}".format(message.decode("utf-8"))
        clientIP  = "Client IP Address: {}:{}".format(address[0], address[1])
    
        print(clientMsg)
        print(clientIP)
        print()
    
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)

except KeyboardInterrupt:
    print("Interrupted!")

# ============================================================================