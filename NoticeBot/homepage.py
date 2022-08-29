from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import requests
import json
import time

html = urlopen("https://ssu.ac.kr/%EA%B5%90%EC%9C%A1-%C2%B7-%EC%97%B0%EA%B5%AC/%EB%8C%80%ED%95%99%EC%86%8C%EA%B0%9C/%EC%9D%B8%EB%AC%B8%EB%8C%80%ED%95%99/")
dp = BeautifulSoup(html, 'html.parser')

inmun = []
#인문대학
for dpname in dp.select('div.vc_custom_1559024152576'):
    for i in dpname.get_text().split():
        inmun.append(i) #인문대학 리스트 하나에 정리하기
for dpname in inmun:
    a = urlopen("https://ssu.ac.kr/%EA%B5%90%EC%9C%A1-%C2%B7-%EC%97%B0%EA%B5%AC/%EB%8C%80%ED%95%99%EC%86%8C%EA%B0%9C/%EC%9D%B8%EB%AC%B8%EB%8C%80%ED%95%99/"+urllib.parse.quote(dpname)) #대학별로 학과소개사이트 열기
    homepage = BeautifulSoup(a, 'html.parser')
    for hp in homepage.select('a.homepage'):
        print(hp.get('href')) #학과소개사이트에 있는 학과홈페이지 바로가기 링크 뽑아오기