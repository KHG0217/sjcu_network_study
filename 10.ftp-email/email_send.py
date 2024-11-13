import smtplib
from email.mime.text import MIMEText

# 네이버 이메일 로그인 정보
user = ''
password = ''

# 이메일 구성
subject = "title test"
content = "body test"
receiver = ''

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = user
msg['To'] = receiver

# 네이버 이메일 서버에 연결
with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
    server.login(user, password)  # 로그인
    server.sendmail(user, receiver, msg.as_string())  # 이메일 발송

print('이메일이 성공적으로 발송되었습니다.')
