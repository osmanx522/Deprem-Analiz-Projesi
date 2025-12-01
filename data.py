import requests
import pandas as pd
from bs4 import BeautifulSoup

class Data:
    def __init__(self,):
        self.deprem_listesi = [] # Deprem Verilerini Saklamak İçin Liste
        self.df = None  # DataFrame Başlangıç Değeri

    def veri_cek(self):
        url = "https://deprem.afad.gov.tr/last-earthquakes.html" # AFAD Son Depremler Sayfası
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            } # Tarayıcı Bilgisi
        response = requests.get(url, headers=header) # Sayfayı İndirme
        if response.status_code == 200: # Başarılı İstek Durumu
            return response # Başarılı İstek
        else:
            return [None, f"Veri çekme hatası: {response.status_code}"] # Hata Durumu

    def veri_isle(self, response):
        if response: # Geçerli Yanıt Var mı?
            soup = BeautifulSoup(response.content, "html.parser") # HTML İçeriğini Parse Etme
            table = soup.find("table", class_ = "content-table") # Deprem Tablosunu Bulma
            if table:  # Tablo Var mı?
                tbody = table.find("tbody") # Tablo Gövdesini Bulma
                rows = tbody.find_all("tr") # Tüm Satırları Alma
                print(f"{len(rows)} Tane Deprem Verisi Bulundu.") # Toplam Deprem Sayısını Yazdırma
                for row in rows: # Her Satır İçin
                    cols = row.find_all("td") # Sütunları Alma
                    if len(cols) >= 7: # Yeterli Sütun Var mı?
                        veri = {
                            "Tarih": cols[0].text.strip(), # Tarih Bilgisi
                            "Enlem": cols[1].text.strip(), # Enlem Bilgisi
                            "Boylam": cols[2].text.strip(), # Boylam Bilgisi
                            "Derinlik (km)": cols[3].text.strip(), # Derinlik Bilgisi
                            "Tipi": cols[4].text.strip(), # Deprem Tipi
                            "Büyüklük": cols[5].text.strip(), # Büyüklük Bilgisi
                            "Yer": cols[6].text.strip() # Yer Bilgisi
                        } # Deprem Verilerini Sözlük Olarak Saklama
                        self.deprem_listesi.append(veri) # Listeye Ekleme
        else:
            return response[1] # Hata Mesajını Yazdırma

    def dataframe_olustur(self): # DataFrame Oluşturma Metodu
        self.veri_isle(self.veri_cek()) # Veriyi Çekme ve İşleme
        self.df = pd.DataFrame(self.deprem_listesi) # Deprem Verilerini DataFrame'e Dönüştürme

if __name__ == "__main__":
    data = Data()
    data.dataframe_olustur()