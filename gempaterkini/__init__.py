import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    '''
    Tanggal : 24 Agustus 2021
    Waktu : 12:05:52 WIB
    Magnitudo : 4.0
    Kedalaman : 40 Km
    Lokasi : LS=1.48 BT=134.01
    Pusat Gempa : Pusat gempa berada di darat 18 Km Barat laut Ransiki
    Dirasakan : Dirasakan (Skala MMI): II-III Manokwari, II-III Ransiki
    :return:
    '''
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        tanggalwaktu = soup.find('span', {'class': 'waktu'})
        tanggalwaktu = tanggalwaktu.text.split(', ')
        tanggal = tanggalwaktu[0]
        waktu = tanggalwaktu[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        #print(magnitudo)
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1

        result = 0

        # print(content.text)
        # soup = BeautifulSoup(content)
        # print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = tanggal #'24 Agustus 2021'
        hasil['waktu'] = waktu #'12:05:52 WIB'
        hasil['magnitudo'] = magnitudo #'12:05:52 WIB'
        hasil['kedalaman'] = kedalaman #'40 Km'
        hasil['koordinat'] = {'ls':ls, 'bt':bt} #{'ls': 3.82, 'bt': 133.45}
        hasil['lokasi'] = lokasi #'Pusat gempa berada di darat 18 Km Barat laut Ransiki'
        hasil['dirasakan'] = dirasakan #'Dirasakan (Skala MMI): II-III Manokwari, II-III Ransiki'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak menemukan data gempa terkini')
        return

    hasil = dict()
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Dirasakan : {result['dirasakan']}")

# if __name__ == '__main__':
#     print('Ini adalah package gempa terkini')