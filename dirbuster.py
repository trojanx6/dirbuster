try:
    from bs4 import BeautifulSoup as btu 
    import requests as req 
    import sys,os
    import time
except:
    os.system("pip install requests")
    os.system("pip install beautifulsoup4 ")
    

print("""

><><><><><><><><><><><><><><><><><><><><><><>

      |________DirBuster_________|

~~~> coder by: spygoldeye

~~~> version:1.v [ trial version ] 

>>> [ python dirbuster.py  https://www.example.com ] <<<

><><><><><><><><><><><><><><><><><><><><><><>""")















site = input(sys.argv[0])
#site = "https://www.dictionary.com"
dosya = open('tr.txt','r') # Dosyayı açıyoruz
dirb = dosya.readlines() # satır satır okuyoruz
dosya.close() # kapatıyoruz dosyayı
for dir in dirb: # döngüye alıp dosyayı dongü bitine kadar devam ediyor
    url = site+'/'+dir
   # time.sleep(0.3) kararsızım bundq
    istek = req.get(url) # get  ile istek gönderiyoruz
    asl = btu(istek.content, "lxml") # web kazıma işlemine başlıyoruz, site html indiriyoruz
    al = asl.find_all(string=["404: Bu sayfa bulunamadı", "404: This page could not be found","Page Not Found","404 Not Found","404"]) # site kodlarinda bunları ariyor
    if len(al) == 0: # geri dönüşte ise içinde sayılacak bir sey yoksa Found yazicak
        print("[+] Found {url}")
    else:
        print("Not Found ") # else ilede geri donerse Not Found olucak
