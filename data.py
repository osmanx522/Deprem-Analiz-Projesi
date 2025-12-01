import requests
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

deprem_listesi = [] # Deprem Verilerini Saklamak İçin Liste

def veri_cek():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html" # AFAD Son Depremler Sayfası
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        } # Tarayıcı Bilgisi
    response = requests.get(url, headers=header) # Sayfayı İndirme
    return response

def veri_isle(response):
    if response.status_code == 200: # İndirme Başarılı mı?
        soup = BeautifulSoup(response.content, "html.parser") # HTML İçeriğini Parse Etme
        table = soup.find("table", class_ = "content-table") # Deprem Tablosunu Bulma
        if table:
            tbody = table.find("tbody") # Tablo Gövdesini Bulma
            rows = tbody.find_all("tr") # Tüm Satırları Alma
            print(f"{len(rows)} Tane Deprem Verisi Bulundu.") # Toplam Deprem Sayısını Yazdırma
            for row in rows: # Her Satır İçin
                cols = row.find_all("td") # Sütunları Alma
                if len(cols) >= 0: # Yeterli Sütun Var mı?
                    veri = {
                        "Tarih": cols[0].text.strip(),
                        "Enlem": cols[1].text.strip(),
                        "Boylam": cols[2].text.strip(),
                        "Derinlik (km)": cols[3].text.strip(),
                        "Tipi": cols[4].text.strip(),
                        "Büyüklük": cols[5].text.strip(),
                        "Yer": cols[6].text.strip()
                    } # Deprem Verilerini Sözlük Olarak Saklama
                    deprem_listesi.append(veri) # Listeye Ekleme
                else:
                    return ("Yeterli sütun bulunamadı.")
            else:
                # Verileri DataFrame'e Dönüştürme
                return pd.DataFrame(deprem_listesi)
        else:
            return("Deprem tablosu bulunamadı.")
    else:
        return(f"Sayfa indirilemedi. Durum Kodu: {response.status_code}")

if __name__ == "__main__":
    df = veri_isle(veri_cek()) # Veriyi Çekme, İşleme ve DataFrame'e Dönüştürme
    # Bütün verileri yazdırma
    print(df)