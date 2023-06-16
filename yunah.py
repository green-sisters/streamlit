import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime
import platform
from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt
import uuid
import json
import time
#import cv2
import requests
import re

# OCR 인식 함수
def OCR(upload_file):
  api_url = 'https://8cbdvua55p.apigw.ntruss.com/custom/v1/22878/18b029032c74f9dc3223fcfe629227edf8e8880be05ecf50148ea52dae003f79/general'
  secret_key = 'R1hjd3JEam9pT3ZRTmRNRkxPTG9MVWhqanpxQmRoeHk='

  request_json = {
      'images': [
          {
              'format': 'jpg',
              'name': 'demo'
          }
      ],
      'requestId': str(uuid.uuid4()),
      'version': 'V2',
      'timestamp': int(round(time.time() * 1000))
  }

  payload = {'message': json.dumps(request_json).encode('UTF-8')}
  files = [
    ('file', upload_file)
  ]
  headers = {
    'X-OCR-SECRET': secret_key
  }

  response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
  hangul_pattern = re.compile('[가-힣]+')

  # 정규표현식 패턴에 매칭되는 모든 한글 단어를 추출하여 리스트에 저장
  hangul_words = hangul_pattern.findall(response.text)
  
  word_choice = ['다회용기','개인컵','다회용컵','에코별']

  count = 0
  used = []
  for word in hangul_words:
      for target_word in word_choice:
          if target_word in word:
            count += 1
            used.append(target_word)
  setence = ', '.join(used)
  point = 10 * count
  print(setence,'을(를) 사용하셨군요!',f'{point}포인트가 지급되었습니다!')
  
  
  
  
  
  
  
### 앱 화면 ###  
st.title('에코리지')
st.header("Ecollege")

option = st.selectbox('서비스를 선택해주세요',
                       ('영수증 적립','쓰레기 배출'))
st.write(option,'하러 가볼까요?')

if option == '영수증 적립':
    upload_file = st.file_uploader('사진을 업로드 해주세요', type=['jpg', 'png', 'jpeg'])
    if upload_file is not None:
      # 이미지 열기
      image = Image.open(upload_file)
      image = image.resize((256,512))
      st.image(image)
      # OCR
      OCR(upload_file)
      
      
        
if option == '쓰레기 배출':
  trash_option = st.selectbox('어떤 종류의 쓰레기를 배출하나요?',
                       ('유리','캔','플라스틱'))
  # trash_option이랑 모델 결과가 같으면 
  # trash_option을 배출했어요. 포인트는 ~~
