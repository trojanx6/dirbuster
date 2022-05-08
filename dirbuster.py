from bs4 import BeautifulSoup as btu  

import requests as req 




print("""

><><><><><><><><><><><><><><><><><><><><><><>

      |________DirBuster_________|

~~~> coder by: spygoldeye

~~~> version:1.v [ trial version ] 

>>> [ python dirbuster.py ] <<<

><><><><><><><><><><><><><><><><><><><><><><>""")

site = input("Hedef site giriniz: ")

#te = "https://www.dictionary.com"

dosya = open('tr.txt','r') 

dirb = dosya.readlines()

dosya.close() 

for dir in dirb:

    url = site+'/'+dir  

    istek = req.get(url) 

    asl = btu(istek.content, "lxml") 

    al = asl.find_all(string=["404: Bu sayfa bulunamadı",

     "404: This page could not be found","Page not found!","404 Not Found","404"]) 

    if len(al) == 0: 

        print(f"[+] Found {url}")

    elif istek.status_code == "503":

        print(" Not Found")

    else:

        print("Not Found ") 
