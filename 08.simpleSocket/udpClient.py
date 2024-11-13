import socket

# UDP 소켓 생성
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 9999

# 데이서 송수신
while True:
    sendData = bytes(input('Input : ').encode())
    if not sendData: 
        break
    clientSocket.sendto(sendData, (HOST, PORT))
    recvData, addr = clientSocket.recvfrom(1024) 
    print('Server >> Client : ' + recvData.decode())
    
# 소켓 종료    
clientSocket.close()