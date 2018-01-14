
import cv2  #open cv kütüphanemizi import ediyoruz
import numpy as np #numpy kütüphanemizi ekliyoruz.

def laplace_Filtresi():#laplace fonksiyonunu tanımlıyoruz
    for i in range(baslangicxkoordinati, baslangicxkoordinati + filtreninxkoordinati):#filtremizi satırlara uygulamak için döngü
        for j in range(baslangicykoordinati, baslangicykoordinati + filtreninykoordinati): #filtremizi sütunlara uygulamak için döngü
            value = int((-1 * pikseldizisi[i - 1, j - 1]) + (-1 * pikseldizisi[i - 1, j]) + (-1 * pikseldizisi[i - 1, j + 1]) + (-1 * pikseldizisi[i, j - 1]) + (
                8 * pikseldizisi[i, j]) + (-1 * pikseldizisi[i][j + 1]) + (-1 * pikseldizisi[i + 1, j - 1]) + (-1 * pikseldizisi[i + 1, j]) + (#
                -1 * pikseldizisi[i + 1][j + 1])) #laplas filtremis [-1 ; -1; -1, -1; -8; -1, -1;-1;-1] olduğu için bu değerlerle çarpıyoruz
            if value < 0: # değer 0 dan küçük oldug durumlar için yaptık
                value = 0

            if value > 255:  #değer 255ten büyükse 255 alabilmek için if statement ı oluşturduk
                value = 255

            print("Piksele Yazılacak Değer: " + str(value))
            resim[i, j] = value#filtrenin uygulanacağı bölgeye değeri yazdık

    cv2.imshow('Filtre_Uygulanmis_Resim', resim) #resmimizi göstermesi için
    cv2.imwrite("out.png", resim) # değişiklikleri out.png ye atmak için
    pass

def mean_fltr():#ortalama (mean) filtresi için gerekli fonksiyon
    if (osize == 3): #params.txt dosyasında 3 okursa buraya girecek
        for i in range(baslangicxkoordinati, baslangicxkoordinati + filtreninxkoordinati):
            for j in range(baslangicykoordinati, baslangicykoordinati + filtreninykoordinati):
                k = int((pikseldizisi[i - 1, j - 1] + pikseldizisi[i - 1, j] + pikseldizisi[i - 1, j + 1] + pikseldizisi[i, j - 1] + pikseldizisi[i, j] + pikseldizisi[i, j + 1] + pikseldizisi[i + 1, j - 1] + pikseldizisi[i + 1, j] + pikseldizisi[i + 1][j + 1]) / (osize * osize))
                print("Piksele Yazılacak Değer: " + str(k))
                resim[i, j] = k#bulduğumuz elemanı fotoğraftaki değiştirilecek piksele atıyoruz.

    elif (osize == 5):#params.txt dosyasında 5 okursa buraya girecek
        for i in range(baslangicxkoordinati, baslangicxkoordinati + filtreninxkoordinati):
            for j in range(baslangicykoordinati, baslangicykoordinati + filtreninykoordinati):
                k = int(
                    pikseldizisi[i, j] + pikseldizisi[i][j + 1] + pikseldizisi[i + 1, j - 2] + pikseldizisi[
                        i + 1, j - 1] + pikseldizisi[i + 1, j] + pikseldizisi[i + 1][
                        j + 1] + pikseldizisi[i + 1, j + 2]+ pikseldizisi[i + 2, j] + pikseldizisi[i + 2, j + 2] + pikseldizisi[i + 2, j + 1] + pikseldizisi[i - 1, j - 2] + pikseldizisi[i - 1, j + 2] +
                    pikseldizisi[i - 1, j - 1] + pikseldizisi[i - 1, j] + pikseldizisi[i - 1, j + 1] + pikseldizisi[i, j + 2] + pikseldizisi[i, j - 1] +
            pikseldizisi[i - 2, j - 2] + pikseldizisi[i - 2, j - 1] + pikseldizisi[i - 2, j] + pikseldizisi[
                i - 2, j + 1] + pikseldizisi[i - 2, j + 2] + pikseldizisi[
                i + 2, j - 2] + pikseldizisi[i + 2, j - 1]) /(osize * osize) # 5 x5 filte için gerekli olan pikseller
                print("Piksele Yazılacak Değer: "  +str(k) )
                resim[i, j] = k#bulduğumuz elemanı fotoğraftaki değiştirilecek piksele atıyoruz.
    else:
        print("Filtre Boyutu Yanlış..")

    cv2.imshow('Filtrelenmis', resim)
    cv2.imwrite("out.png", resim)
    pass
def median_fltr():#median_fltr filtresinin uygulandıgı fonksiyonu tanımlıyoruz.
    for z in range(baslangicxkoordinati, baslangicxkoordinati + filtreninxkoordinati):
        for y in range(baslangicykoordinati, baslangicykoordinati + filtreninykoordinati): #Filtre uygulayacağımız pikselleri listeye atmak için değişkenlere atıyoruz.
            Listemiz = [int(pikseldizisi[z - 2, y - 2]),int(pikseldizisi[z - 2, y - 1]), int(pikseldizisi[z - 2, y]), int(pikseldizisi[z - 2, y + 1]),int(pikseldizisi[z - 2, y + 2]),int(pikseldizisi[z + 2, y - 2]),int(pikseldizisi[z + 2, y - 1]),
            int(pikseldizisi[z + 2, y]), int(pikseldizisi[z + 2, y + 2]), int(pikseldizisi[z + 2, y + 1]),int(pikseldizisi[z - 1, y - 2]),int(pikseldizisi[z - 1, y + 2]),int(pikseldizisi[z - 1, y - 1]),int(pikseldizisi[z - 1, y]), int(pikseldizisi[z - 1, y + 1]),
            int(pikseldizisi[z, y - 2]), int(pikseldizisi[z, y + 2]),int(pikseldizisi[z, y - 1]), int(pikseldizisi[z, y]),int(pikseldizisi[z][y + 1]),int(pikseldizisi[z + 1, y - 2]), int(pikseldizisi[z + 1, y - 1]),int(pikseldizisi[z + 1, y]),int(pikseldizisi[z + 1][y + 1])
            ,int(pikseldizisi[z + 1, y + 2])]

            orta_deger = 12  # filtremiz 5x5 sabit oldugu için ortadaki değere 12 indisiyle ulaşıcaz
            Listemiz.sort()#listede ki elemanları küçükten büyüğe sıralıyoruz.
            print("Piksele Yazılacak Değer: " + str(Listemiz[orta_deger]))
            resim[z, y] = Listemiz[orta_deger]#bulduğumuz elemanı fotoğraftaki değiştirilecek piksele atıyoruz.
    cv2.imshow('Filtrelenmis', resim)
    cv2.imwrite("out.png", resim)

    pass



if __name__ == '__main__':

    paramFile = open('params.txt')#params.txtden değer okumak için
    params = paramFile.readlines()#satır satır okumak için

    resimFileName = params[0].split('\n')[0]#ilk satırdan resim ismini okumak için


    koordinatlar = params[1].split(', ')[0]
    baslangicxkoordinati = int(koordinatlar.split(' ')[0])
    baslangicykoordinati = int(koordinatlar.split(' ')[1])
    filtreninxkoordinati = int(koordinatlar.split(' ')[2])
    filtreninykoordinati = int(koordinatlar.split(' ')[3])
    print("Koordinatlarımız: ")
    print(str(baslangicxkoordinati) + " " + str(baslangicykoordinati) + " " + str(filtreninxkoordinati) + " " + str(filtreninykoordinati))

    f1 = params[2].split(', ')[0]#params.txtden 3.satırı(hangi filtre olacağını belirten satır)
    print("Kullanılan Filtre(Harf)")
    print(f1)

    resim = cv2.imread(resimFileName, 0)#resmi okuyoruz
    pikseldizisi = np.array(resim, dtype='int64')#resmin piksellerini diziye atıyoruz
    if f1.split(' ')[0] == 'o': #okuduğumuz 3.satırda mean filtresinin istendiği kontrol ediliyor
        osize = int(f1.split(' ')[1])#mean filtresi için verilen boyutu okuyoruz
        mean_fltr()#mean_fltr fonksiyonunu çağırıyoruz
        print("Mean Filtre Sonlandı")
    satirlar = resim.shape[0]
    sutunlar = resim.shape[1]

    print(resim.shape)

    print(resim[0, 0])
    print(resim[0, 1])
    if f1[0] == 'm':#median_fltr filtresini uygulamak için harf kontrolu yapıyouz.
        median_fltr()#median_fltr fonksiyonunu çağırıyoruz.
        print("Median Filtre Sonlandı")
    if f1[0] == 's':#laplace filtresini uygulamak için harf kontrolu yapıyoruz.
        laplace_Filtresi()#laplace fonksiyonunu çağırıyoruz
        print("Laplas Filtre Sonlandı")

