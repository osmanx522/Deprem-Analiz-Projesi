import requests
from bs4 import BeautifulSoup
url = "https://deprem.afad.gov.tr/last-earthquakes.html" # AFAD Son Depremler Sayfası
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
} # Tarayıcı Bilgisi
response = requests.get(url, headers=header) # Sayfayı İndirme

if response.status_code == 200: # İndirme Başarılı mı?
    soup = BeautifulSoup(response.content, "html.parser") # HTML İçeriğini Parse Etme
    table = soup.find("table", class_ = "content-table") # Deprem Tablosunu Bulma
    if table:
        tbody = table.find("tbody") # Tablo Gövdesini Bulma
        rows = tbody.find_all("tr") # Tüm Satırları Alma
        print(f"Toplam Deprem Sayısı: {len(rows)}") # Toplam Deprem Sayısını Yazdırma
        for row in rows: # Her Satır İçin
            cols = row.find_all("td") # Sütunları Alma
            if len(cols) >= 0: # Yeterli Sütun Var mı?
                tarih = cols[0].text.strip() # Tarih/Saat
                enlem = cols[1].text.strip() # Enlem
                boylam = cols[2].text.strip() # Boylam
                derinlik = cols[3].text.strip() # Derinlik
                tip = cols[4].text.strip() # Tip
                buyukluk = cols[5].text.strip() # Büyüklük
                yer = cols[6].text.strip() # Yer
                print(f"Tarih/Saat: {tarih}, Enlem: {enlem}, Boylam: {boylam}, Derinlik: {derinlik}, Tip: {tip}, Büyüklük: {buyukluk}, Yer: {yer}")
            else:
                print("Yeterli sütun bulunamadı.")
    else:
        print("Deprem tablosu bulunamadı.")
else:
    print(f"Sayfa indirilemedi. Durum Kodu: {response.status_code}")