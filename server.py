# importing libraries
import socket

# Setting up Server Connection.
server = socket.socket()
host = socket.gethostname()
print("Server is starting on: ", host)
port = 8080
server.bind((host, port))
print("Binding of Host and Port completed successfully.")
print("Waiting for Client Connection...")

# Setting up for Client Connection.
server.listen(1)
conn, address = server.accept()
print(address, "is connected to the Server.")

# Loop for sending and receiving messages
while True:
    message_to_send = input(str("Type Msg: "))
    message_to_send = message_to_send.encode()
    conn.send(message_to_send)
    print("Sent.")
    incoming_message = conn.recv(2048)
    incoming_message = incoming_message.decode()
    print("Msg Received: ", incoming_message)
