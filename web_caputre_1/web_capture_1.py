'''
네이버 메인 페이지 캡처하여 png 이미지 파일로 저장

html2image 라이브러리 사용
'''
from html2image import Html2Image

html = Html2Image() # Html2Image() 객체 생성
'''
Html2Image()의 screenshot 메서드 
: 말 그대로 주소 캡처하여 png 파일로 저장
'''
html.screenshot(url='https://www.naver.com/', save_as='naver.png')