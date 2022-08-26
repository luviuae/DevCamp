from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json

#-------------------------------------------------------------------
# 슬랙 봇에 메시지 보내는 거
#-------------------------------------------------------------------
def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text, "attachments": attachments})
Token = 'xoxb-3985950723973-3989033977427-CM9Dpponpkmj02XjOKpBqnJn'

attach_dict = {
    'color' : '#ff0000',
    'author_name' : '새로운 공지사항이 등록되었습니다.',
    'title' : notice.select_one('.subject').get_text(),
    'title_link' : 'http://infocom.ssu.ac.kr'+notice.select_one('.con_box').get('href')
} # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력
attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
#-------------------------------------------------------------------

html = urlopen("http://infocom.ssu.ac.kr/kor/notice/undergraduate.php")
notice = BeautifulSoup(html, 'html.parser')

# 첫 게시물 제목: notice.select_one('.subject').get_text()
# 첫 게시물 링크: notice.select_one('.subject').get('href')

#, encoding='CP949'
with open('./Test.txt', 'rt') as t1:
    test_txt = t1.read()

#새 게시글 올라오면
if (test_txt != notice.select_one('.subject').get_text()):
    with open('./Test.txt', 'w') as t1:
        t1.write(notice.select_one('.subject').get_text()) #파일 텍스트를 새 게시물 제목으로 수정
    notice_message(Token, "#test", "", attach_list) #슬랙 메시지 보냄
#새 게시글 안올라오면
else:
    print('그대로임')



