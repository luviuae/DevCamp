from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
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
