''' 
Linked List:
    * İçerisinde birden fazla veriyi bağlı olarak tutabileceğimiz bir veri yapısı
    * Node(düğüm) ile birbirlerine bağlıdırlar
    * Node'larda iki tane bilgi tutulur
        1) Saklanacak verinin tutulduğu yere pointer ile referans bilgisi
        2) Bağlı olduğu Node'un pointer'ını tutuyor

        Örnek:
        Head                                                                    Tail
        [value: Yunus, next: 2], [value: Can, next: 3], [value: Cengiz, next: None]

        - Son Node'dan sonra yeni bir Node gelmediği için next referans2ı None olur 

    * Araya bir eleman insert etmek istersem sadece kendinden önceki node'un pointer'ını günceller (index kaydırmaz)
    * Ancak o elemanı bulana kadar diğer elemanları gezer.
    * O yüzden prepend(başa ekleme) O(1) de çalışırken ortalara insert etme O(n)
    * Aynı zamanda kendisinden sonra gelecek node'u pointer olarak ekler
    * Bu sayede eleman insert etme işlemi de sabit zamanda O(1) gerçekleşir
    * Burada da eleman okumak lineer zamanda O(n) gerçekleşir
    * En son elemanı almak için ilk elemandan (Head) başlanır ve pointer'ı None olan Node'a kadar ilerlenir    

    
------------------------------------------------------------


Array ve Listelerden Farkı:
    * RAM'de array veya liste elemanları contigous (ard arda) bir yapıda tutuluyorlar
    * Veriler ard arda dizildiği ve ordered yapıda olduğu için array ve listelerde indexleri kullanabiliyoruz
    * Ve listenin/arrayin içindeki herhangi bir elemana sabit zamanda yani O(1)'de erişebiliyoruz
    * Ancak listeye bir eleman insert edildiği zamanda, sonrasında kalan tüm elemanlar yana kaydırıldığı için lineer zamanda O(n) gerçekleşir
    * Yani listelerde bir elemanı almak efektif çalışırken elemanı yazmak (insert ile) daha yüksek complexity'de gerçekleşiyor

    
*** Baştan bir eleman eklemek veya çıkarmak istersek linked list faydali (tüm indexler yer değişmiyor, index yok)
*** Ancak listenin ortasından ekleyeceksek o elemanı bulana kadar tüm elemanları gezeceği için worst scenario2da ikisi de O(n)
*** Herhangi bir elemana index ile erişimde normal listeler O(1) linked list'de index olmadığı için erişim O(n)

------------------------------------------------------------


Linked List Türleri:
    1) Singly Linked List: Sadece değer ve sonraki node pointer'ı tutulur, son node'un pointer'ı None
    2) DOubly Linked List: Değer ve hem önceki hem sonraki Node'un pointer'ları tutulur. 1. Node prev: None, Son Node next: None
    3) Circular Linked List: Doubly gibi ancak son Node'un next 1. Node'u işaret ederken 1. Node prev son Node'u işaret eder

    
Doubly Linked List:
    Örnek:
    Header        <-              ->          Trailer
    [None, Yunus, 2], [1, Can, 3], [2, Cengiz, None]

    * Header ve Trailer'da aslında içi boş Node'lardır


'''