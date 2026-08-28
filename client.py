import socket

# إنشاء سوكيت TCP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 12345))
print(" Connected to server. Type messages below (or 'exit' to quit).")

while True:
    msg = input(" You: ")
    c.sendall(msg.encode())
    if msg.lower() == 'exit':
        print(" You left the chat.")
        break
    data = c.recv(1024).decode()
    print(f" Server: {data}")
    if data.lower() == 'exit':
        print("Server ended the chat.")
        break

c.close()
