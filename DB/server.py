from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__, template_folder='../')

from crawl import crawl_website_ssucatch
# 여기에 크롤링 함수를 복사하거나 import하세요.
# 예: from your_crawling_script import crawl_website_ssucatch

@app.route('/')
def index():
    today_date = '2023.08.23'
    #today_date = datetime.today().strftime('%Y.%m.%d')
    today_temp_data = today_date.replace('.', '-')
    
    # URL과 카테고리 정보
    URL_li = [('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EB%B9%84%EA%B5%90%EA%B3%BC%C2%B7%ED%96%89%EC%82%AC&keyword',"비교과행사"),
        ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EA%B5%AD%EC%A0%9C%EA%B5%90%EB%A5%98&keyword','국제교류'),
        ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EC%9E%A5%ED%95%99&keyword', '장학'),
        ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EB%B4%89%EC%82%AC&keyword','봉사'),
        ('/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?category=%ED%95%99%EC%82%AC&keyword','학사')
    ]

    all_crawled_data = {}
    
    for url, category in URL_li:
        crawled_data = crawl_website_ssucatch(url, today_date)  # 크롤링 함수를 실행
        all_crawled_data[category] = crawled_data  # 카테고리별로 크롤링 데이터 저장

    print(all_crawled_data)
    return render_template('index.html', data=all_crawled_data)

if __name__ == '__main__':
    app.run(debug=True)
