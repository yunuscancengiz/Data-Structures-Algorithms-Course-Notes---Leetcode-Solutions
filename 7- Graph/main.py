'''
Graph: 
    - Ağaçlara benzerler, ağaçlar da Graph'ın daha basit şeklidir
    - Node'lara Vertex de denilebiliyor
    - Branch'lere de Edge denilebiliyor
    - Yapı olarak direkt bir root ve parent - child ilişkisi yoktur
    - Bağlantılar tek yönlü (Directional) veya çift yönlü (Bidirectional) olabilir

--------------------------------------------------------

Graph Türleri:
    1) Weighted Graph:
        * Node'ları bazı değerlere göre ağırlıklarabiliriz 
        * Örnek:
            - 3 adet vertex var, bunlar İstanbul, Lizbon ve Roma
            - Her 3 vertex de birbirine edge'ler ile bağlı 
            - Bu edge'ler bilet fiyatlarına göre ağırlıklandırılmış
            - İstabul - Roma arası 100 eur, Lizbon - Roma arası 10 eur, İstanbul - Lizbon arası 20 eur
            - İstanbul'dan Roma'ya gideceksek ve bizim için önemli olan bilet fiyatı ise İstanbul - Lizbon - Roma rotasını tercih ederiz
            - Ancak bizim için zaman daha önemli ise İstanbul - Roma rotasını tercih ederiz
            - Weighted Graph'lar vertex'ler arası ilişkileri tespit edip karar alma sürecini kolaylaştırabiliriz
            - Veya trafiğin yoğun olduğu ama 10 km sürecek yol yerine trafik yoğnluğu olmayan bir 20 km'lik bir yol tercih edebiliriz
            - Bu ilişki de vertex ve edge yapısı ile kurulabilir

        * Ağırlıklı Graph'larda ağırlık pozitif de negatif de etkiye sahip olabilir
        * Kimisinde bilet fiyatını temsil edip yüksek olunca fazla fiyatı temsil edebilirken
        * Diğerinde kazanılacak parayı temsil edip yüksek olması olumlu bir şeye işaret edebilir

------------------------------------------------------

Adjaceny Matrix:
    -  Yapı olarak çok karmaşık olabileceği için Graph içindeki vertex'lerin arasındaki bağlantıları matrix ile ifade edebiliriz
    - Örnek:
        * A, B, C, D, E vertex'lerine sahip bir Graph var
        * A: E ve B ile bağlantılı (Bidirectional)
        * B: A, D ve C ile bağlantılı (Bidirectional)
        * C: B ile bağlantılı (Bidirectional)
        * D: E ve B ile bağlantılı (Bidirectional)
        * E: A ve D ile bağlantılı (Bidirectional)

        - Matrix:
                A   B   C   D   E

            A   0   1   0   0   1

            B   1   0   1   1   0

            C   0   1   0   0   0

            D   0   1   0   0   1

            E   1   0   0   1   0

        - Bağlı bulunduğu vertex'ler 1 diğerleri 0
        - Örneğin Graph'da sadece E - D arasındaki bağlantıyı değiştirelim
        - Bağlantı E -> D directional olsun
        - Yani D vertex'inden E vertex'ine gidilemesin ama tam tersi yapılabilsin
        - Bunun matrix'i:

                A   B   C   D   E

            A   0   1   0   0   1

            B   1   0   1   1   0

            C   0   1   0   0   0

            D   0   1   0   0   0 (updated col x row)

            E   1   0   0   1   0


    - Aynı zamanda bu bağlantılar matrix haricinde Dictionary - HashMap veya farklı bir deyişle Adjacency List'te tutulabilir
    - Adjacency List:

        {
            'A': ['B', 'E'],
            'B': ['A', 'C', 'D'],
            'c': ['B'],
            'D': ['B', 'E'],
            'E': ['A', 'D']
        }

    - Bağlantıları matrix ile göstermek ile dictionary ile görstermek arasında Space Complexity farkı vardır
    - Space Complexity:
        1) Adjacency Matrix: O(V^2)
            - Vertex sayısının karesi kadar yer kaplar
            - Bağlı olmayan vertex'leri de 0 olarak saklar

        2) Adjacency List: O(V + E)
            - vertex + edge sayısı kadar yer kaplar
            - bağlı olmayan durumlar gösterilmediği için sadece vertex ve edge (bağlantı) sayısı kadar yere ihtiyaç vardır


    - Time Complexity - Insert Vertex işlemi:
        1) Adjacency Matrix: O(V^2)
            - Yeni bir kolon eklemek için matrix'de tüm matrix baştan yazdırılıyor 
        
        2) Adjacency List: O(1)
            - Direkt dict sonuna yeni bir liste eklenebilir, tüm dict'i dolaşmaz


    - Time Complexity - Insert Edge işlemi:
        1) Adjacency Matrix: O(1)
            - Sadece 1 değeri matrix üzerinde günceller 
        
        2) Adjacency List: O(1)
            - Sadece 1 değeri dict üzerinde günceller 


    - Time Complexity - Delete Vertex İşlemi:
        1) Adjacency Matrix: O(V^2)
            - Kolon silindikten sonra tüm matrix en baştan yazılır
        
        2) Adjacency List: O(V + E)
            - Vertex ve Edge sayısı kadar işlem yapılır


    - Üstteki işlemler için hem space complexity hem de time complexity açısından dictionary'leri kullanmak daha verimli
    - Matrix ise delete edge işleminde time complexity açısından daha verimlidir

    - Tİme Complexity - Delete Edge İşlemi:
        1) Adjacency Matrix: O(1)
            - Matrix üzerinde bir edge ve bağlı olduğu vertex'teki bilgi anında silinebilir (col x row yapısı)
        
        2) Adjacency Matrix: O(E)
            - Dict üzerinde edge'i sildikten sonra aynı edge'i diğer vertex'lerden de silmek için edge sayısı kadar işlem gerekir 


            
'''