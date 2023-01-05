'''
Aplikasi Deteksi Gempa Terkini
Modularisasi dengan Function
'''
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
