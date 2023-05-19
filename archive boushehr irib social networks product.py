import requests as req
from bs4 import BeautifulSoup

link = 'http://boushehr.irib.ir/cyber?p_p_id=101_INSTANCE_WgTvGnX1pEb6&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_101_INSTANCE_WgTvGnX1pEb6_delta=20&_101_INSTANCE_WgTvGnX1pEb6_keywords=&_101_INSTANCE_WgTvGnX1pEb6_advancedSearch=false&_101_INSTANCE_WgTvGnX1pEb6_andOperator=true&p_r_p_564233524_resetCur=false&cur='
text = ""
last_page = 1884//20 + 1
for page in range(1, last_page+1):
    print(f"page = {page}, progress = {((page*10000)//(last_page+1))/100} %")
    r = req.get(link + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    musics_column = soup.find(id="column-1")
    for item in musics_column.find_all('a'):
        if item.text == 'تولیدات فضای مجازی' or item.find('img') is not None:
            continue
        try:
            item['class']
            break
        except:
            pass
        # print(item)
        text += f"Name : {item.text.strip()},\t\t\t(link)[{item['href']}]\n"

with open("clip_name.txt", 'w', encoding="utf-8") as file:
    file.writelines(text)
