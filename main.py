import data   # data.py içindeki Data sınıfını kullanacağız
def main():
    deprem_data = data.Data()   # Sınıftan nesne oluştur
    deprem_data.dataframe_olustur()   # DataFrame oluşturma metodunu çağır
    return deprem_data.df   # Oluşturulan DataFrame'i döndür
df = main()
if __name__ == "__main__":
    print(df.head())   # DataFrame'i yazdır