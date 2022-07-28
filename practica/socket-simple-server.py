import socket

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen(1)
  print('Esperando conecciones...')
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      data = conn.recv(1024)
      if not data: break
      conn.sendall(data)