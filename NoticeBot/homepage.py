from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import requests
import json
import time

#예전 계획 (보류)
#html = urlopen("https://ssu.ac.kr/%EA%B5%90%EC%9C%A1-%C2%B7-%EC%97%B0%EA%B5%AC/%EB%8C%80%ED%95%99%EC%86%8C%EA%B0%9C/%EC%9D%B8%EB%AC%B8%EB%8C%80%ED%95%99/")
#dp = BeautifulSoup(html, 'html.parser')
#
#inmun = []
##인문대학
#for dpname in dp.select('div.vc_custom_1559024152576'):
#    for i in dpname.get_text().split():
#        inmun.append(i) #인문대학 리스트 하나에 정리하기
#for dpname in inmun:
#    a = urlopen("https://ssu.ac.kr/%EA%B5%90%EC%9C%A1-%C2%B7-%EC%97%B0%EA%B5%AC/%EB%8C%80%ED%95%99%EC%86%8C%EA%B0%9C/%EC%9D%B8%EB%AC%B8%EB%8C%80%ED%95%99/"+urllib.parse.quote(dpname)) #대학별로 학과소개사이트 열기
#    homepage = BeautifulSoup(a, 'html.parser')
#    for hp in homepage.select('a.homepage'):
#        print(hp.get('href')) #학과소개사이트에 있는 학과홈페이지 바로가기 링크 뽑아오기

#  'creativewriting', 'ssfilm', 'sports'는 사이트 형식이 다르다..
인문대학 = ['docs', 'korlan', 'englan', 'gerlan', 'france', 'chilan', 'japanstu', 'philo', 'history']
#"https://"+인문대학+".ssu.ac.kr/%ed%95%99%ea%b3%bc%ec%82%ac%eb%ac%b4%ec%8b%a4%ec%95%8c%eb%a6%bc/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/"
for inmun in 인문대학:
    html = urlopen("https://"+inmun+".ssu.ac.kr/%ed%95%99%ea%b3%bc%ec%82%ac%eb%ac%b4%ec%8b%a4%ec%95%8c%eb%a6%bc/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/)")
    docs = BeautifulSoup(html, 'html.parser')
    print('< '+inmun+' >')
    for i in docs.find_all('table', class_='t_list'):
        for j in i.find_all('tr', class_=False):
            for k in j.find_all('td', class_='title'):
                for l in k.find_all('a', class_=False):
                    print(l.get_text())
#자연과학대학 =
#수학과 : https://math.ssu.ac.kr/?page_id=977&term_id&paged=(페이지개수) 'table.t_list > a.href'
