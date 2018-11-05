import requests
from bs4 import BeautifulSoup

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


page = get_html('https://torrenthaja.com/bbs/board.php?bo_table=torrent_drama')
soup = BeautifulSoup(page, 'html.parser')
drama_area = soup.find("div",{"class": "board-list-body"}).find_all \
    ("div",{"class": "td-subject ellipsis"})
    
for drama_index in drama_area:
    _title = drama_index.text.strip()
    url_soup = drama_index.find("a")
    _url = url_soup["href"]
    print(_title, _url)
    
    
'''
[결과 예시]
뷰티 인사이드.E11.181105.1080p-NEXT https://torrenthaja.com/torrent_drama/19167.html
계룡선녀전.E01.181105.1080p-NEXT https://torrenthaja.com/torrent_drama/19166.html
계룡선녀전.E01.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19165.html
뷰티 인사이드.E11.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19164.html
비켜라 운명아.E01.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19163.html
끝까지 사랑.E66.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19162.html
차달래 부인의 사랑.E46.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19161.html
나도 엄마야.E110.181105.720p-NEXT https://torrenthaja.com/torrent_drama/19160.html
플레이어.E12.181104.1080p-NEXT https://torrenthaja.com/torrent_drama/19159.html
나인룸.E10.181104.720p-NEXT https://torrenthaja.com/torrent_drama/19158.html
내 사랑 치유기 15-16회 합본.E08.181104.1080p-NEXT https://torrenthaja.com/torrent_drama/19157.html
내 사랑 치유기 15-16회 합본.E08.181104.720p-NEXT https://torrenthaja.com/torrent_drama/19156.html
내 사랑 치유기 13-14회 합본.E07.181104.720p-NEXT https://torrenthaja.com/torrent_drama/19155.html
플레이어.E12.181104.720p-NEXT https://torrenthaja.com/torrent_drama/19154.html
내 사랑 치유기 13-14회 합본.E07.181104.1080p-NEXT https://torrenthaja.com/torrent_drama/19153.html
'''
