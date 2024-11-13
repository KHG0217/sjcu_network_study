import socket

HOST = '127.0.0.1'
PORT = 9999              

# UDP 소켓 생성 및 서버 주소 정보 할당
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((HOST, PORT))

# 데이터 수신 및 전송
while True:
  data, addr = serverSocket.recvfrom(1024)
  print('Client >> Server : ' + data.decode())
  serverSocket.sendto(data, (addr))

# 소켓 종료
serverSocket.close()