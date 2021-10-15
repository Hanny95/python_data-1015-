from bs4 import BeautifulSoup as bs
from urllib import request as rq
import time

# 데이터 가져오기
url = 'https://www.naver.com/'
naverData = rq.urlopen(url).read()
naverText = naverData.decode('UTF-8')

# 시간 함수
def getCurrentTime():

   return time.strftime('[%Y-%m-%d %I:%M:%S]')

# 인덱스 함수
def convertIntToString(idx):

    return '[' + str(idx) + ']'

# 데이터 분석하기
soup = bs(naverText, 'html.parser')
aTags = soup.find_all('a')

# a 테그의 속성 가져오기
for idx, ele in enumerate(aTags):
    print(f'idx : {idx}, \t eleStr : {ele.string}, \t href : {ele.attrs["href"]}')


# for idx, element in enumerate(aTags):
#     try:
#         with open('C:/chh_scraping/download/naverA.txt', 'a') as f:
#             f.write(f'{getCurrentTime()} {convertIntToString(idx)} {element.string} \n')
#
#     except Exception as e:
#         print(e)
#         print('Fail')
#
#     else:
#         print('Success')