'''
Searching Algorithms:
    Sequential vs Binary:
        * Bir listede bir sayı aradğımızı düşünelim
        * Sequential search yapılırsa tüm liste teker teker dolaşılır ve Time Complexity: O(n)
        * Eğer liste sıralıysa binary search yapabiliriz
        * Binary search listenin tam ortasındaki elemandan başlar, aranan değerle karşılaştırır 
        * Eğer aranan değer daha küçükse listenin başından ortasına kadar olan kısmı bir daha iikiye böler
        * Eğer daha büyükse de listenin ortasından sonuna kadar olan kısmı ikiye böler
        * Sayıyı bulana kadar veya listede sayının olmadığını tespit edene kadar bu şekilde devam eder
        * Listede eleman sayısı 2 katına çıksa dahi işlem sayısı sadece 1 artar
        * O yüzden binary search'ün Time Complexity: O(log n)


HashTable:
    * Python'daki dictionary'lerdir.
    * Listede indexten bağımsız bir eleman bulmaya çalışırlen O(n) zamanda çalışır
    * Ancak HashTable'da bir eleman bulmak istersek O(1) zamanda çalışır
    * Çünkü saklanan değer bir Hash Fonksiyonu ile hashlenir ve ona göre hafızada saklanacağı adres belirlenir
    * Sonrasında değeri aramak istediğimizde yine Hash Fonksiyonuna sokar, çıkan sonucun hafızadaki değerini getirir
    * Eğer değeri saklarken heashlenmiş sonuca ait slot zaten doluysa en yakın slota atar
    * Bazı kaynaklarda HashTable'da aramanında Time Complexity'si O(n) olarak geçer
    * Bu hash fonksiyonunun tüm değerler için aynı slot'u işaret etmesi ve değerlerin en yakın boş slota atılması durumunu ele almak içindir
    * Worst Scenario'dur ve gerçekleşme ihtimali çok çok düşüktür o sebeple Time Complexity: O(1) şeklinde düşünülebilir

'''