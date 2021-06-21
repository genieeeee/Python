#!/usr/bin/env python
# coding: utf-8

# # Python Opencv 얼굴인식

# 표준 데스크탑 환경 용 패키지 (Windows, macOS, 거의 모든 GNU / Linux 배포)
# 
# pip install opencv-python #메인 모듈 만 필요한 경우 실행
# 
# pip install opencv-contriv-python #기본 및 contrib 모듈이 모두 필요한 경우 실행

# # 1) 얼굴일식 및 메모장 실행

# In[1]:


import cv2
import subprocess

#얼굴 인식 캐스케이드 파일 읽는다
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0)
 
while (True):
    # frame 별로 capture 한다
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    # 사용자 얼굴이 인식되었을 경우, 메모장 실행
    #인식된 얼굴 갯수를 출력
    if len(faces) == 1:
        notepad = ("C:\\Windows\\notepad.exe")
        # 바로 프로그램 실행
        subprocess.call(notepad)
        break
        
    # 인식된 얼굴에 사각형을 출력한다
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    #화면에 출력한다
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
 
cap.release()
cv2.destroyAllWindows()


# # 2) 얼굴인식 및 이미지 캡쳐 후 이메일 전송

# In[2]:


import cv2
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
 
while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
       
    if len(faces) == 1:
        #capture
        cv2.imwrite('C:\\Users\\yunjin\\Desktop\\python_source\\openCV\\img_capture.jpg', gray)
        
        # 지메일 아이디,비번 입력하기
        email_user = 'test@naver.com'     #<ID> 본인 계정 아이디 입력
        email_password = 'asdfa'          #<PASSWORD> 본인 계정 암호 입력
        email_send = 'test@naver.com'     # <받는곳주소> 수신자 이메일 abc@abc.com 형태로 입력

        # 제목 및 수,발신자 설정
        subject = 'Warning!!!' 

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        # 본문 내용 입력
        body = 'Please check the picture'
        msg.attach(MIMEText(body,'plain'))

        # 첨부파일 경로/이름 지정하기
        filename = 'C:\\Users\\yunjin\\Desktop\\python_source\\openCV\\img_capture.jpg'  
        attachment = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= " + filename)
        msg.attach(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.naver.com',587)
        server.starttls()
        server.login(email_user,email_password)

        server.sendmail(email_user,email_send,text)
        server.quit()
                
        break;
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
 
cap.release()
cv2.destroyAllWindows()


# In[ ]:




