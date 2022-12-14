import socket

# Create TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007  
mBuffer=1024

print('Iniciando el servidor up on {} port {}'.format(HOST, PORT))
sock.bind((HOST, PORT))
# Listen for incoming connections
sock.listen(1)

while True:
  # espera la conn.
  print('Esperando conectar con un cliente')
  connection, client_address = sock.accept()
  try:
    print('Conectado desde', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
      print('-------------------------------')
      data = connection.recv(mBuffer)#16
      print('Recibiendo dato: {!r}'.format(data))
      
      if data:
        print('Enviando respuesta al cliente')
        connection.sendall(data)
      else:#No existe datos, client_address
        break
  except KeyboardInterrupt:
    break
  finally:
    # Clean up the connection
    connection.close()