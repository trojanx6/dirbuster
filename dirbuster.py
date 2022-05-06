import os

try:

    from bs4 import BeautifulSoup as btu 

except ModuleNotFoundError as hata:

    os.system("pip install beautifulsoup4 ")

    os.system("pip install requests")

    os.system("clear")

import requests as req

import sys

import time

    

    

    

    

print("""

><><><><><><><><><><><><><><><><><><><><><><>

      |________DirBuster_________|

~~~> coder by: spygoldeye

~~~> version:1.v [ trial version ] 

>>> [ python dirbuster.py  https://www.example.com ] <<<

><><><><><><><><><><><><><><><><><><><><><><>""")

#site = input(sys.argv[0])

site = "https://www.dictionary.com"

dosya = open('tr.txt','r') # Dosyayı açıyoruz

dirb = dosya.readlines() # satır satır okuyoruz

dosya.close() # kapatıyoruz dosyayı

for dir in dirb: # döngüye alıp dosyayı dongü bitine kadar devam ediyor

    url = site+'/'+dir

    

    

   # time.sleep(0.3) kararsızım bunda

    istek = req.get(url) # get  ile istek gönderiyoruz

    asl = btu(istek.content, "lxml") # web kazıma işlemije başlıyoruz, site html indiriyoruz

    al = asl.find_all(string=["404: Bu sayfa bulunamadı", "404: This page could not be found","Page Not Found","404 Not Found","404"]) # site kodlarinda bunları ariyor

    if len(al) == 0: # geri dönüşte ise içinde sayılacak bir sey yoksa Found yazicak

        print(f"[+] Found {url}")

    elif istek.status_code == "503":

        print("Not Found")

    else:

        print("Not Found ") # else ilede geri donerse Not Found olucak
