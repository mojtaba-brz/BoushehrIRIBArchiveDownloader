import requests as req
import numpy as np
from bs4 import BeautifulSoup 
from time import sleep
# Config ----------------------------------------------------
site_main_address = 'http://boushehr.irib.ir'
file_name = 'music_name.txt'
files_save_dir = 'downloaded musics from boushehr irib' # Note: directory must be existed
# ----------------------------------------------------------

def is_connected(host='http://google.com'):
    try:
        a = req.get(host)
        if a.status_code == 200:
            return True
        else:
            return False
    except:
        return False
    
links = np.array([], dtype=np.string_)
with open(file_name, 'r', encoding="utf8") as file:
    for line in file:
        links = np.append(links, line.split()[-1][7:-1])

total_links_count = len(links)        
for i in range(544, total_links_count):
    print(f"index = {i}, progress = {(i/total_links_count)*100:>0.2f} %\tlink : {links[i]}")
    download_retring_counter = 0
    while True:
        try:
            r = req.get(links[i])
            break
        except:
            print("retrying for page")
            sleep(10)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        download_link = soup.find(class_="asset-full-content-body").find('p').find('a')
    except:
        continue
    if download_link is None:
        print('no download link')
        continue
    else:
        download_link = site_main_address + download_link['href']
        file_format = download_link.split('.')[-1]
        while download_retring_counter < 3:
            try:
                r = req.get(download_link, allow_redirects = True)
                break
            except:
                print(f"retrying for download, link : {download_link}")
                if is_connected:
                    download_retring_counter += 1
                else:
                    sleep(10)
    with open(f"{files_save_dir}/{i}.{file_format}", 'wb') as file:
        file.write(r.content)
i += 1
print(f"index = {i}, progress = {(i/total_links_count)*100:>0.2f} %")
