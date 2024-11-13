import socket

# TCP 소켓 생성
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 8888

# 서버에 연결
clientSocket.connect((HOST, PORT))

# 데이터 송수신
while True:
    sendData = bytes(input('Input : ').encode())
    if not sendData: 
        break
    clientSocket.send(sendData)
    recvData = clientSocket.recv(1024).decode() 
    print('Server >> Client : ' + str(recvData))

# 소켓 연결 종료
clientSocket.close()