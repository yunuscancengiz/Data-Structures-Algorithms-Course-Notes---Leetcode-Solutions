''' 
Big O Notaition: Yazılan kodun karmaşıklığını ifade eder. 

    * Time Complaxity & Space Complexity
    * Hem zaman karmaşıklığı hem de yer karmaşıklığı (Kodun çalışması ne kadar sürüyor? Hafızada ne kadar alan tutuyor vs.)
    * Kodun ne kadar verimli, efektif çalıştığını tespit etmekte kullanılır
    * Kaynak: https://www.bigocheatsheet.com/
    * Sıralama (Kötüden iyiye): O(n!) > O(2^n) > O(n^2) > O(n log n) > O(n) > O(log n) > O(1)
'''

# O(n) için örnek bir fonksiyon -> n sayıda elemanı tek tek dolaşır
# n=5 için 5 işlem
def bigOn(n):
    for i in range(n):
        print(n)


# O(n^2) için örnek fonksiyon -> n sayıda eleman için n^2 kadar işlem yapar
# n=5 için 25 işlem
def bigOn2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# O(n^3) için örnek -> n sayıda eleman için n^3 kadar işlem
# n=5 için 125 işlem
def bigOn3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)


# O(log n) için örnek -> logaritmik artar, n'deki çok yüksek artış işlem sayısını lineer veya üstel olarak artırmaz
# n=32 için 5 işlem
import math

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)


# O(n log n) örneği -> içeride logaritmik artan bir while döngüsü var o kısım için complexity O(log n)
# Aynı zamanda while loop içinde bir de lineer artan bir for loop var o kısım da O(n)
# Yani bu fonksiyon için complexity: O(n log n)
# n=32 için n * log n = 32 * 5 = 160 işlem yapılır
def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n)
        for i in range(lim):
            print(i)


# ------------------------------------------
# O(n log n) Neden önemli?
# 
#   Genel olarak sorting algoritmalarında worst senaryoda O(n^2) gibi çok uçuk time complexity değerleri ile karşılaşılıyor
#   Genelde en verimli çalışanları O(n log n) complexity'e sahip olanlardır ve onlar daha yaygın kullanılır
#  
# ------------------------------------------


# Space Complexity Örneği
# Bize bir liste verildiğini ve bu listedeki sayıları dizmemiz istendiğini düşünelim
# numbers = [3, 5, 2, 4]
# yeni bir liste oluşturmadan aynı liste üzerinde yer değiştirerek yaparsak space complexity O(1)
# yeni bir listeye atıp orada dizsek space complexity O(n)
# Space complexity genel olarak bu şekilde değişiyor, time complexity kadar farklı değil
# O(n) space complexity'e sahip bir algoritmayı o(1)'e çeivrmeye çalışırken time complexity artabilir
# Yani ihtiyacımıza göre space complexity'i düşürmek için time complexity'den feragat edebiliriz veya tam tersi