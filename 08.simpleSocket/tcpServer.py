import socket

HOST = '127.0.0.1'  
PORT = 8888        

# TCP 소켓 생성
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 주소 정보 할당 후 접속 대기 상태로 전환
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

# 연결 수락
conn, addr = serverSocket.accept()
print('Connected by' + str(addr))

# 데이터 수신 및 전송
while True:
  data = conn.recv(1024)
  if not data:
    break
  print('Client >> Server : ' + data.decode())
  conn.send(data)

# 소켓 연결 종료
conn.close()
serverSocket.close()