from ftplib import FTP

# FTP 서버 연결
ftp = FTP()
ftp.connect('192.168.56.1', 21)  # FTP 서버의 IP와 포트
ftp.set_pasv(False)  # Active 모드 설정

# 로그인
ftp.login(user='root', passwd='team1234')

# 여기에서 여러 FTP 작업을 수행할 수 있습니다.
# 예를 들어, 서버의 파일 목록을 가져옵니다.
ftp.retrlines('LIST')

# 로그아웃 및 연결 종료
ftp.quit()
