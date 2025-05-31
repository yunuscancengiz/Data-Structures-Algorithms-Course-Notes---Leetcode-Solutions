''' 
Tree:
    * Linked List'ler gibi Node'lardan oluşan ve Node2lar ile birbirine bağlanan yapılardır
    * Parent veya Root yani kök ve ona bağlı olan dallar ve yapraklar (child veya leaf)ile birbirine bağlanarak ilerler
    * Eğer child Node'a bağlı olan bir Node yoksa leaf olarak adlandırılır
    * Child Node'lar da kendilerine bağlı olan Node'lar için Parent Node görevi görür


Binary Search Tree

                38  (Root)
        19              69  (Child)
    12      24      59      95  (Leaf)

    * Binary Search Tree'ler arama algoritmalarıdır
    * Root'dan başlanarak her bir Node 2 dala ayrılarak ilerler
    * Soldaki Node'un değeri Parent Node'dan küçük, sağdaki Node'un değeri ise büyüktür

Binary Search Tree Big O Gösterimi
    * Her bir adımda ikiye bölünerek ilerliyoruz
    * Yani eleman sayısı 2 katına çıksa bile fazladan tek bir Node kontrol ediliyor
    * Yani time complexity logaritmik olarak artıyor
    * O yüzden arama veya Node ekleme gibi işlemler için complexity O(log n) diyebiliriz (Average Scenario)

    Ancak:
        * Node eklerken sürekli olarak parent node'dan büyük değer geldiğini varsayalım.
        * Sürekli olarak parent node'un sağına ekleme yaparız

                38  
                    69  
                        95

        * Bu durumda Linked List'ler gibi tek bir daldan oluşan bir yapımız olur
        * Bu durum worst scenario'dur ve örneğin 95'i bulmak için 3 elemanın tamamını gezmemiz gerekir
        * Yani worst scenario'da time complexity O(n)

        * Bu senaryo teorik olarak doğru olsa bile pratikte binary search tree'nin mantığına ters bir durumdur
        * Yani teoride complexity: O(n), pratikte complexity: O(log n) gibi düşünülebilir 


------------------------------------------------------------

Recursion:
    * İç içe geçme durumudur
    * Bir fonksiyonun kendi içinde tekrar çağrılması
    * Bir veri yapısının kendi instance'ını kendi içinde kullanması
    *  
'''