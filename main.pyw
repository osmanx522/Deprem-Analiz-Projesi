import earthquake_data   # data.py dosyasını içe aktar
from PyQt5 import QtWidgets, QtCore, QtGui  # PyQt5 modüllerini içe aktar


def main():
    deprem_data = earthquake_data.Data()   # Sınıftan nesne oluştur
    deprem_data.dataframe_olustur()   # DataFrame oluşturma metodunu çağır
    return deprem_data.df   # Oluşturulan DataFrame'i döndür
df = main()
if __name__ == "__main__":
    print(df.head())   # DataFrame'i yazdır