# importing libraries
import socket

# Setting up Connection with Server.
server = socket.socket()
host = input(str("Enter Server Address/Hostname: "))
port = 8080
server.connect((host, port))
print("Connection Successful.")

# Loop for sending and receiving messages
while True:
    incoming_message = server.recv(2048)
    incoming_message = incoming_message.decode()
    print("Msg Received: ", incoming_message)
    message_to_send = input(str("Type Msg: "))
    message_to_send = message_to_send.encode()
    server.send(message_to_send)
    print("Sent.")
