import requests as req
from bs4 import BeautifulSoup

link = 'http://boushehr.irib.ir/cyber?p_p_id=101_INSTANCE_xIONcIF2C5Xl&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_101_INSTANCE_xIONcIF2C5Xl_delta=8&_101_INSTANCE_xIONcIF2C5Xl_keywords=&_101_INSTANCE_xIONcIF2C5Xl_advancedSearch=false&_101_INSTANCE_xIONcIF2C5Xl_andOperator=true&p_r_p_564233524_resetCur=false&cur='
text = ""

for page in range(1, 143):
    print(f"page = {page}, progress = {((page*10000)//142)/100} %")
    r = req.get(link + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    musics_column = soup.find(id="column-2")
    for item in musics_column.find_all('a'):
        if item.text == 'موسیقی و پادکست' or item.find('img') is not None:
            continue
        try:
            item['class']
            break
        except:
            pass
        # print(item)
        text += f"music name : {item.text.strip()}, (link)[{item['href']}]\n"

with open("music_name.txt", 'w', encoding="utf-8") as file:
    file.writelines(text)
