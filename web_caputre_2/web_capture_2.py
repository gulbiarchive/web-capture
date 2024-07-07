from html2image import Html2Image

# 한 번에 여러 페이지 캡처하기
# 리스트 형태로 url 주소들과 저장할 이미지 파일명을 각각 전달e
html = Html2Image()
html.screenshot(url=['https://www.naver.com/', 'https://www.google.co.kr/?hl=ko'],
                save_as=['naver.png', 'goole.png'])