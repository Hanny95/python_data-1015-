from urllib import request as rq
from urllib import parse as ps
from bs4 import BeautifulSoup as bs

rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

locationCode = {'stnId':'133'}
params = ps.urlencode(locationCode)


rssURL = rssURL + '?' + params
print(f'rssURL : {rssURL}')

rssData = rq.urlopen(rssURL)

bsObj = bs(rssData, 'html.parser')
# title = bsObj.select_one('title')
# print(f'{title.string}')
#
# titles = bsObj.select('title')
# print(f'{len(titles)}')
#
# for title in titles:
#     print(f'{title.string}')


# description
# header

title = bsObj.select_one('description > header > title')
print(f'title : {title.string}')

tm = bsObj.select_one('description > header > tm')
print(f'title : {tm.string}')

wf = bsObj.select_one('description > header > wf')
print(f'title : {wf.string}')

# data 하위 테그 값 찾기

modes = bsObj.select('data > mode')
tmefs = bsObj.select('data > tmef')
wfs = bsObj.select('data > wf')
tmns = bsObj.select('data > tmn')
tmxs = bsObj.select('data > tmx')
rnsts = bsObj.select('data > rnst')

for i in range(len(modes)):
    print(f'mode: {modes[i].string}')
    print(f'tmefs: {tmefs[i].string}')
    print(f'wfs: {wfs[i].string}')
    print(f'tmns: {tmns[i].string}')
    print(f'tmxs: {tmxs[i].string}')
    print(f'rnsts: {rnsts[i].string}')
    print('=' * 30)
