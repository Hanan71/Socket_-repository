import socket

# إنشاء سوكيت TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))  # IP محلي + منفذ 12345
s.listen()

print(" Server is listening on port 12345...")

# انتظار اتصال العميل
conn, addr = s.accept()
print(f" Connected to client: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print(" Client disconnected.")
        break
    print(f"💬 Client: {data}")
    msg = input(" Server: ")
    conn.sendall(msg.encode())
    if msg.lower() == 'exit':
        print(" Server ended the chat.")
        break

conn.close()
s.close()
