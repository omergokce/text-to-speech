from gtts import gTTS  # pip install gtts
from random import randint
import os

while True:
    # input'dan textdeki satıları alıyor

    a = input(">>> ")

    # input'a girilen metni google translate olarak okuyor.
    #toplu girişler için metni bir text dosyasına alt alta ekleyip kopyalayın ve programı çalıştırınca direk yapıştırın. Ben 500 kişiye kadar denedim çalışıyor.
    audio = gTTS(text=a, lang='tr')
    name = a+ ".mp3"



    # sesi textteki isme göre kaydediyor
    audio.save(name)
    # okan sesinin adyny doredyar


    # dosya başarıyla oluşturulunca otomatik olarak çalıştırıp dinletiyor.Bunu devre dışı bıraktım. Aktif edebilirsiniz
    
    #os.system(name)