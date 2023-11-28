import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from multiprocessing import Pool

# 0 : 비교과행사
# 1 : 국제교류
# 2 : 장학
# 3 : 봉사

# catch_li 리스트와 매치되는 URL LIST
URL_li = [('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EB%B9%84%EA%B5%90%EA%B3%BC%C2%B7%ED%96%89%EC%82%AC&keyword',"비교과행사"),
    ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EA%B5%AD%EC%A0%9C%EA%B5%90%EB%A5%98&keyword','국제교류'),
    ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EC%9E%A5%ED%95%99&keyword', '장학'),
    ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EB%B4%89%EC%82%AC&keyword','봉사'),
    ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?category=%ED%95%99%EC%82%AC&keyword','학사')
]

# # 오늘 날짜를 YYYY.MM.DD 형식으로 가져옴
# today_date = datetime.today().strftime('%Y.%m.%d')
today_date = '2023.08.23'
today_temp_data = today_date.replace('.', '-')

# 슈캐치 - 장학 크롤링
def crawl_website_ssucatch(category_url, today_date):
    BASE_URL = "https://scatch.ssu.ac.kr"
    URL = BASE_URL+category_url

    today_news = []

    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, "html.parser")
        ul_element = soup.select_one(".notice-lists")
        
        # ul 내부의 모든 li 태그들을 선택
        li_elements = ul_element.select("li")

        # 오늘 날짜와 일치하는 항목만 필터링 및 해당 항목의 href 값을 가져옴

        for li in li_elements:
            news_text = li.text.strip()
            if news_text.startswith(today_date):
                news_link = li.find('a')['href']

                span_tags = li.find_all('span')
                span_texts = [span.text.strip() for span in span_tags]
                if news_link.startswith("/"):
                    full_link = BASE_URL + news_link
                else:
                    full_link = news_link
                
                # 이미지 파일 링크와 텍스트를 분리
                news_text = span_texts[-1]

                # 제목, 링크, 내용(이미지는 이미지 링크), 요약된 내용을 리스트에 추가
                today_news.append((news_text, full_link))
        
        print(today_news)
    except requests.RequestException as e:
        print(f"Error occurred while fetching {URL}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {URL}: {e}")

    return today_news

crawl_website_ssucatch()