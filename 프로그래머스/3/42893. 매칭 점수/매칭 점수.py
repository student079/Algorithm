# 기본 점수 : 검색어가 등장하는 횟수(대소문자 무시)
# 외부 링크 수 : 다른 외부 페이지로 연결된 링크의 개수
# 링크 점수: 링크 걸린 다른 웹페이지의 기본점수 / 외부 링크 수
# 매칭 점수 : 기본 점수 + 링크 점수

# pages 20개
# 페이지 길이 1500
# 3만 문자

# 페이지 딕셔너리
# 키: 페이지 url, value [기본 점수, 외부 링크 수 , 링크들, 링크 점수]

from collections import defaultdict
import re

def solution(word, pages):
    answer = 0
    
    pageDict = dict()
    
    for page in pages:
        ps = page.split('\n')
        cnt = 0
        name = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        links = re.findall('<a href="(https://[\S]*)"', page)
        for p in ps:
            cnt += countWord(p, word)
                
        pageDict[name] = [cnt, len(links), links ,0]
    
    # 링크 점수 계산
    keys = pageDict.keys()
    for url in keys:
        cnt, cntOut, links, linkScore = pageDict[url]
        for link in links:
            if link in keys:
                a, b, c, d = pageDict[link]
                d += cnt / cntOut
                pageDict[link][3]=d
    
    idx = 0
    scores = []
    for url in keys:
        scores.append((pageDict[url][0] + pageDict[url][3], idx))
        idx += 1
    scores.sort(key = lambda x: (-x[0], x[1]))
    
    return scores[0][1]


def getUrl(line):
    exiosLink = re.findall('<a href="(https://[\S]*)"', line)
    print(exiosLink)
    idx = line.index("https://")
    idx += 8
    res = ""
    while line[idx] != "\"":
        res += line[idx]
        idx+=1
    return res

def countWord(line, word):
    line = line.lower()
    ps = re.split(r'[^a-zA-Z]+', line)
    cnt = 0
    word = word.lower()
    for p in ps:
        if p == word:
            cnt+=1
    return cnt
    