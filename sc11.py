from urllib import request as rq
from bs4 import BeautifulSoup as bs

url = 'https://browse.gmarket.co.kr/search?keyword=%EB%82%98%EC%9D%B4%ED%82%A4%EC%9A%B4%EB%8F%99%ED%99%94'
htmlData = rq.urlopen(url)

htmlObj = bs(htmlData, 'html.parser')

names = htmlObj.select('#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title')
# print(f'{names}')


# for name in names:
#     print(f'name : {name}')

# for name in names:
#     name = list(name)
#     print(f'name[2]: {name[2]}')
    # for idx, item in enumerate(name):
    #   print(f'idx : {idx}, \t item : {item}')


#========== 신발 가격 데이터
prices = htmlObj.select('#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong')
print(f'prices : {prices}')

# for price in prices:
#     price = list(price)
#     print(f'{price[1]}')

for price in prices:
    price = list(price)
    print(f'price[1]: {price[1]}')
    # for idx, item in enumerate(price):
    #     print(f'idx : {idx}, item : {item}')
