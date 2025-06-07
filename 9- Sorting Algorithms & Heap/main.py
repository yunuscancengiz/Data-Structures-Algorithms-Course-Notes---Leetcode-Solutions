'''
Sorting Algorithms:
    - Kaynak: https://visualgo.net/en

    1- Bubble Sort:
        * 0. index'ten başlar (i=0)
        * i ve i + 1 kıyaslanır eğer i > i + 1 ise yerleri değiştirilir
        * i = i + 1 olarak güncellenir ve yine i ve i + 1 kıyası yapılır
        * Bu şekilde listedeki en büyük eleman tespit edilir ve son index'e taşınır
        * Sonra yine i = 0 olarak başlanır ve aynı işlemler tekrarlanır
        * Ancak artık son index kontrol edilmez, çünkü en büyük değer oraya taşındı ve kontrol edilmesi gereksiz olur
        * 2. en büyük değer de sondan bir önceye taşınır ve artık o index de kontrol edilmez
        * Bu şekilde max_index 0'a düşene kadar veya herhangi iki değerin yeri artık değişmeyene kadar devam edilir
        * Time Complexity: O(n^2)

    2- Selection Sort:
        * Yine ilk index'ten başlanır (i = 0)
        * minimum değerin index'i bir değişkende saklanır
        * Her sayı minimum sayıyla karşılaştırılır ve minimum sayıdan küçük bir sayı varsa minimum değişkeni o index ile güncellenir
        * Döngü sonunda minimum değişkenindeki index ile 0. index'teki eleman yer değiştirir
        * Minimum değer artık 0. index2e taşındığı için artık 0. index kontrol edilmez ve 1. index'ten başlanır
        * Aynı işlem yapılır ve minimum index ile 1. index elemanları yer değiştirir ve 2. indexten döngü tekrar başlanır
        * Bu şekilde listedeki tüm elemanlar kontrol edilene kadar devam eder
        * Time complexity: O(n^2)

    3- Insertion Sort:
        * 1. index'ten başlanır (i = 1)
        * i. index’teki eleman, solundaki elemanlarla kıyaslanır
        * Eğer kendisinden büyük bir eleman varsa, bu eleman bir sağa kaydırılır
        * Bu işlem, i. eleman kendisinden küçük bir elemana ulaşana kadar devam eder
        * Uygun pozisyon bulunduğunda i. eleman oraya yerleştirilir
        * Sonra i = i + 1 yapılır ve aynı işlemler tekrar edilir
        * Böylece her adımda i’ye kadar olan kısım sıralı hale gelir
        * Listenin sonuna kadar bu şekilde devam eder
        * Time Complexity: O(n^2)

    4- Merge Sort:
        * Dizi ortadan ikiye bölünür (recursive olarak)
        * Her alt parça, tek eleman kalana kadar tekrar bölünmeye devam eder
        * Daha sonra bu alt diziler, sıralı şekilde birleştirilerek geri toplanır
        * İki sıralı dizi birleştirilirken, ilk elemanları karşılaştırılır ve küçük olan yeni diziye eklenir
        * Karşılaştırma yapıldıkça elemanlar sırayla yerleştirilir
        * Tüm alt diziler birleştikçe, sonunda tamamen sıralı bir dizi elde edilir
        * Divide and Conquer (böl ve fethet) yaklaşımı kullanır
        * Time Complexity: O(n log n)

    5- Quick Sort:
        * Bir pivot eleman seçilir (genellikle ilk, son ya da ortanca eleman)
        * Dizi, pivot’tan küçükler ve büyükler olarak iki gruba ayrılır
        * Pivot’un solunda küçükler, sağında büyükler olacak şekilde dizilir
        * Pivot artık doğru yerde olduğu için bir daha yer değiştirmez
        * Sol ve sağ taraftaki alt diziler için aynı işlem recursive olarak tekrarlanır
        * Her adımda alt diziler daha da küçülerek sıralı hale gelir
        * In-place çalışır, yani ekstra bellek kullanımı azdır
        * Time Complexity: O(n log n) (worst case: O(n^2), kötü pivot seçilirse) (worst scenario: sıralı liste verilmesi)


Heap:
    * Ağaçlara benzer bir veri yapısıdır
    * En önemli özelliği parent'ın child'lardan büyük olma zorunluluğudur
    * Eğer eklenen child, parent'dan küçük ise parent ile child yer değiştirilir
    * Bir diğer önemli özelliği ise Binary Tree'dir yani her parent'a bağlı 2 child vardır
    * BST'den farklı olarak root'un solunda küçükler sağında büyükler olmak zorunda değildir
    * Ancak parent > child kuralından dolayı büyük değerler yukarı doğru toplanır otomatikmen (max heap - tersi olursa min heap)
    * Soldan sağa doğru elemanlar eklenerek devam eder, her parent'a 2 child bağlı olduktan sonra en soldaki child'dan başlanır
    * Ve onlar parent haline gelir 2 child bağlanır ve sağa doğru ilerler
    * Yani ağaç dalları sağa veya sola doğru çarpık olmaz
    
    * Aynı zamanda Heap'ler liste ve ağaç arasında çok hızlı geçiş yapabilirler
    * Çünkü root 1 olacak ve soldan sağa 2, 3, 4... şeklinde devam edecek şekilde index değerleri tutulur
    * Bunlar pozisyon olarak geçerler ama index olarak da düşünüp kullanabiliriz
'''