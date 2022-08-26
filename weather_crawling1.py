from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
#import warnings
#warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

html = urlopen("https://weather.naver.com/")
weather = BeautifulSoup(html, 'html.parser')

k = 50 #비눈 k% 이상 (임의 설정)
n = 1 #n시간 후 날씨 확인 (임의 설정)
current_time = datetime.now()
hour = current_time.hour + n

#for link in weather.find_all('th', id="_idHourly-20220824"+str(hour)):
#    print(link.get('id'))

print(weather.find("th", id="_idHourly-20220824"+str(hour)))

#--------------------------------

def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text, "attachments": attachments})

Token = 'xoxb-3985950723973-3989033977427-CM9Dpponpkmj02XjOKpBqnJn' # 자신의 Token 입력
str1_title = '오늘의 증시 KOSPI 2021-09-17 (금)'
str2 = 'test 메시지를 보냅니다.'
str3 = 'string 3 입니다'

#색깔별로 날씨 나타내는 것도 괜찮을듯

attach_dict = {
    'color' : '#ffff00',
    'author_name' : 'Slack Bot Weather Forecast',
    'title' : '1시간 후 비가 올 예정입니다',
    'title_link' : 'http://weather.naver.com'
    #'text' : str3,
    #'image_url' : 'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png?sidcode=1632301488333'
} # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력

attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
notice_message(Token, "#test", "", attach_list)