from bs4 import BeautifulSoup
html = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>tempHTML document</title>
</head>

<body>

	<div class="top"> 

		<div>top</div>

	</div>

	<div class="nav"> 

		<div class="menu_wrap">
			<a href="#none">menu01</a> &nbsp;&nbsp;
			<a href="#none">menu02</a> &nbsp;&nbsp;
			<a href="#none">menu03</a> &nbsp;&nbsp;
		</div>


	</div>

	<div class="section"> 

		<div class="section_wrap">
			<h1>NEWS DESK</h1>
			<p id="news_desk" class="news">9시 뉴스입니다!</p>

			<h2>오늘 주요 뉴스</h2>
			<p id="today_news" class="news">오늘 뉴스입니다. 드디어 코로나19가 종식되었습니다. 마스크 벗으세요 !!</p>

			<h2>오늘 날씨</h2>
			<p id="today_weather" class="news">간절기에 접어들며 일교차가 큽니다. 감기 조심하세요</p>

			<h2>스포츠 뉴스</h2>
			<p id="sports_news" class="news">한국 여자 배구 올림픽 4강 진출</p>

		</div>


	</div>

	<div class="bottom"> 

		<div>CopyRigh</div>

	</div>

</body>
</html>
'''

path = 'C:/chh_scraping/download'
fileName = 'test.txt'

try:
    with open('C:/chh_scraping/download/test.txt', 'w') as f:
        soup = BeautifulSoup(html, 'html.parser')
        pTags = soup.find_all('p')
        for idx, element in enumerate(pTags):
            str = f.write(element.string + '/n')
        with open(path + fileName, 'r') as f:
            str = f.read()

except Exception as e:
    print(e)
    print('Fail')

else:
    print('Success')

finally:
    print('Done')
