''' 
Tree Traversal:
    * Ağaçlarla ilgili problemleri çözerken neredeyse tamamında Tree Traversal yapmamız gerekecek.
    * Örneğin bir değeri ararken veya ağacı ters çevirirken tüm node'ları teker teker dolanıyoruz
    * Çünkü listeler gibi bir index'leri vs bulunmuyor sadece parent node ve ona bağlı child veya leaf'ler var
    * Bu sebeple direkt olarak index üzerinden değere ulaşamayacağımız için Tree Traversal yapıyoruz

    
Tree Traversal Türleri:
    * İkiye ayrılır
    * Örnek ağaç:

                38
        19              69
    12      24      59      95

    1) BFS (Breadth First Search): 
        - Root node'dan başlar önce bir alt katmana iner soldan sağa onları alır
        - Sonra bir alt katmana iner ve böyle ilerler
        - Önce genişliği alarak gider
        - BFS ile listeye dönüştürmüş olsak sıralama aşağıdaki gibi olacaktı
        - Liste: [38, 19, 69, 12, 24, 59, 95]

    
    2) DFS (Depth First Search):
        - BFS aksine önce derinlik ile ilgilenir
        - Önce her katmandaki tüm node'ları gezmez
        - Genel olarak soldan sağa olarak uygulanır ancak sağdan sola şekilde de kullanılabilir
        - Root node'dan başlar soldaki node'a iner ve sürekli sol node'u alarak en alta (derinliğe) ulaşır
        - En alta inince önce aynı parent'a bağlı olan sağdaki leaf'i alır
        - Ondan sonra parent'a çıkar ve aynı şekilde onun sağını alır bu şekilde ilerler
        - DFS ile listeye dönüştürmüş olsak sıralama aşağıdaki gibi olurdu
        - Liste: [38, 19, 12, 24, 69, 59, 95]


    * Her iki yöntem de farklı amaçlar için birbiri yerine tercih edilebilir
    * Örneğin bir ağaçtaki en küçük değer aranıyorsa en sol altta olacağı için DFS tercih etmek mantıklı olacaktır
    * Veya en büyüğü arıyorsak da sağdan sola uygulayabileceğimiz için yine DFS kullanmak mantıklı olacaktır
'''