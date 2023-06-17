import streamlit as st
from PIL import Image
import requests
import json
import time
import uuid
import cv2
import tempfile

# ...

#네이버 OCR API 설정
api_url = "https://qbt6a09jgb.apigw.ntruss.com/custom/v1/22868/ac35c97ba497dcff3abfab41716ba8999a7cc322edd363f9ce1876512a1dd152/general"
secret_key = 'dVdKZmpqSWpRUnh3c3d2Vmd1ZE1tVVhZbXd4cVdVVnU='

# ...

def main():
    st.title("Ecollege")
    # ...
    st.container()
    st.markdown("""
        <div style="background-color: #f6f5d0; color: #000000; padding: 10px;">
            실물 영수증 사용 시 80 point  <br>
            전자 영수증 사용 시 100 point  <br>
            하루 적립 가능 최대 300 point. <br>
        </div>
    """, unsafe_allow_html=True)

#b-* 문자 인식 함수 정의
def ocr_naver(image_bytes):
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
    files = [('file', ("filename.jpg", image_bytes))]
    headers = {'X-OCR-SECRET': secret_key}

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        result = response.json()
        text = '\n'.join([item['inferText'] for item in result['images'][0]['fields']])
        return text
    else:
        return "Error : " + response.text

def add_points(amount):
    pass

if __name__ == '__main__':
    main()
