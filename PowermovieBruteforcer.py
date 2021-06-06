import asyncio
import requests


def cal_caseprint(input, pre_c, Id):
    last = (len(input) == 1)
    n = len(input[0])
    for i in range(n):
        item = pre_c + input[0][i]
        if last:        
            Id.append(item)
        else:          
            cal_caseprint(input[1:], item, Id)

def BruteForce(message):
    arr = message.replace("?","0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_").replace("!","048AEIMQUYcgkosw").split()
    if arr == []:
        Hi = input('찍을 코드를 입력해주세요.\n>')
        BruteForce(Hi)
    poss = 1
    VideoId = []
    new = []
    for x in arr:
        poss = poss * len(x)
        new.append(list(x))
    if poss > 10000:
        Hi = input('경우의 수가 10000개가 넘어가 작업을 취소합니다. (' + str(poss) + '개)\n또 찍을 코드가 있다면 입력해주세요.\n> ')
        BruteForce(Hi)
    print('\n대입을 시작합니다. (경우의 수 ' + str(poss) + '개)')
    
    cal_caseprint(new,'', VideoId)

    for z in VideoId:
        URL = 'https://img.youtube.com/vi/' + z + '/mqdefault.jpg'
        response = requests.get(URL)
        if response.status_code == 200:
            print('\n\n[영상 링크를 발견했습니다!]\nhttps://youtu.be/' + z + '\n\n')
    Hi = input('대입이 끝났습니다. 또 찍을 코드가 있다면 입력해주세요.\n> ')
    BruteForce(Hi)

Hi = input('찍을 코드를 입력해주세요.\n> ')
BruteForce(Hi)