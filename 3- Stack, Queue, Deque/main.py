'''
Stack:
    * Listelere benzer
    * Ordered yapıdadır, yani indexlerle 0,1,2,3,... gibi ilerler
    * eleman eklemeye push, eleman atmaya pop denir
    * LIFO (Last In First Out) yani listeye son giren ilk çıkar
    * Normal bir listede istenilen index'e veri eklenip çıkarılabilirken burada yapılamaz
    * Top & Base referansı: ilk elemanların bulunduğu kısım base iken son elemanların bulunduğu kısım Top olarak adlandırılır

        Top     5
                4
                3
                2
                1
        Base    0

    * (Yukarıdakiler değer değil index olarak düşünülebilir...)
    * Mantık olarak yemekhanedeki tepsiler gibi düşünülebilir.
        - Temiz tepsiler üst üste dizilir
        - Bir tepsi alınacağında önce en üstteki yani son koyulan alınır (LIFO)

        
---------------------------------------------------------------------

Queue:
    * Ordered yapıdadır
    * Tam olarak banka sırası mantığında çalışır, ilk giren ilk çıkar 
    * FIFO (Firt In First Out)
    * İlk girenlerin bulunduğu kısım Front olarak, son girenlerin bulunduğu kısımda rear olarak adlandırılır.

        Rear                    Front
            5   4   3   2   1   0
        Enqueue                 Dequeue
    * Push veya Pop yerine Enqueue ve Dequeue kullanılır.
    * Enqueue: sıraya al, Dequeue: Sıradan çıkar

    
--------------------------------------------------------------------

Deque:
    * Ordered yapıdadır
    * Push ve Pop yerine Add ve Remove kullanılır
    * Hem baştan hem de sondan ekleme ve çıkarma yapmak mümkündür
    * İlk girenlerin bulunduğu kısım Front olarak, son girenlerin bulunduğu kısımda rear olarak adlandırılır.

        Rear                    Front
        Remove                  Add
            5   4   3   2   1   0
        Add                     Remove

    * Bu özelliği sebebiyle Çift Taraflı Queue (Double-Ended Queue) olarak da bilinir


------------------------------------------------------------------

Python'da Stack

    * Python'da direkt olarak bu veri yapıları bulunmaz, kütüphanelerden import edilerek kullanılabilir
    * Ona rağmen direkt olarak Stack diye bir şey yoktur
    * Çünkü stack mantık olarak python'daki listeler gibi çalışır
    * Eleman sona eklenir ve sondan atılır
    * Ancak stack isimli bir kullanım olmamasına rağmen LifoQueue olarak kullanılabilir

        from queue import LifoQueue 

        şeklinde import edilerek kullanılabilir

    * Kullanım:
        from queue import LifoQueue
        lifo_queue = LifoQueue()
        lifo_queue.put(10)      # [10]
        lifo_queue.put(25)      # [10, 25]
        lifo_queue.get()        # [10]  -> pops 25 and prints it
        lifo_queue.get()        # []    -> pops 10 and prints it

-------------------------------------------------------------------

Python'da Queue

    * Yine kütüphaneden import edilerek kullanılabilir
    * Kullanımı

        from queue import Queue
        my_queue = Queue()
        my_queue.put(10)    # [10]
        my_queue.put(25)    # [10, 25]
        my_queue.get()      # [25]  -> pops 10 and prints it
        my_queue.get()      # []    -> pops 25 and prints it


-------------------------------------------------------------------

Python'da Deque

    * Yine kütüphaneden import edilerek kullanılabilir
    * Kullanımı

        from collections import Deque
        my_deque = Deque()
        my_deque.append(10)         # [10]
        my_deque.appendleft(25)     # [25, 10]
        my_deque.appendleft(15)     # [15, 25, 10]
        my_deque.append(30)         # [15, 25, 10, 30]
        my_deque.pop()              # [15, 25, 10]
        my_deque.popleft()          # [25, 10]
        
'''